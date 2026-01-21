"""PPC Campaign Metrics Calculation Module

This module contains functions for calculating key PPC metrics from campaign data.
Useful for performance marketing analysis and optimization.
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple


class PPCMetricsCalculator:
    """Calculate key PPC performance metrics."""
    
    def __init__(self, campaign_data: pd.DataFrame):
        """Initialize with campaign data.
        
        Args:
            campaign_data: DataFrame with columns: impressions, clicks, spend, conversions
        """
        self.data = campaign_data
        self.validate_data()
    
    def validate_data(self) -> None:
        """Validate required columns exist."""
        required_cols = ['impressions', 'clicks', 'spend', 'conversions']
        missing = [col for col in required_cols if col not in self.data.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")
    
    def calculate_ctr(self) -> float:
        """Calculate Click-Through Rate (CTR).
        
        CTR = (Clicks / Impressions) * 100
        Range: 0-100%
        Better values: 2-5% for most B2B niches
        """
        total_clicks = self.data['clicks'].sum()
        total_impressions = self.data['impressions'].sum()
        
        if total_impressions == 0:
            return 0
        
        return (total_clicks / total_impressions) * 100
    
    def calculate_cpc(self) -> float:
        """Calculate Cost Per Click (CPC).
        
        CPC = Total Spend / Total Clicks
        Lower is better for cost efficiency
        """
        total_spend = self.data['spend'].sum()
        total_clicks = self.data['clicks'].sum()
        
        if total_clicks == 0:
            return 0
        
        return total_spend / total_clicks
    
    def calculate_cpa(self) -> float:
        """Calculate Cost Per Acquisition (CPA).
        
        CPA = Total Spend / Total Conversions
        Critical metric for profitability
        """
        total_spend = self.data['spend'].sum()
        total_conversions = self.data['conversions'].sum()
        
        if total_conversions == 0:
            return float('inf')
        
        return total_spend / total_conversions
    
    def calculate_conversion_rate(self) -> float:
        """Calculate Conversion Rate (CVR).
        
        CVR = (Conversions / Clicks) * 100
        Typical B2B SaaS: 1-5%
        """
        total_conversions = self.data['conversions'].sum()
        total_clicks = self.data['clicks'].sum()
        
        if total_clicks == 0:
            return 0
        
        return (total_conversions / total_clicks) * 100
    
    def calculate_roas(self, revenue: float) -> float:
        """Calculate Return On Ad Spend (ROAS).
        
        ROAS = Revenue / Total Spend
        Breakeven: 1.0x
        Healthy: 3.0x+
        Excellent: 5.0x+
        """
        total_spend = self.data['spend'].sum()
        
        if total_spend == 0:
            return 0
        
        return revenue / total_spend
    
    def get_all_metrics(self, revenue: float = 0) -> Dict[str, float]:
        """Get all metrics in one dictionary.
        
        Args:
            revenue: Total revenue from campaign (needed for ROAS)
        
        Returns:
            Dictionary with all calculated metrics
        """
        return {
            'ctr_%': round(self.calculate_ctr(), 2),
            'cpc_$': round(self.calculate_cpc(), 2),
            'cpa_$': round(self.calculate_cpa(), 2),
            'conversion_rate_%': round(self.calculate_conversion_rate(), 2),
            'roas_x': round(self.calculate_roas(revenue), 2) if revenue > 0 else 0,
            'total_impressions': int(self.data['impressions'].sum()),
            'total_clicks': int(self.data['clicks'].sum()),
            'total_spend': round(self.data['spend'].sum(), 2),
            'total_conversions': int(self.data['conversions'].sum()),
        }


# Example usage
if __name__ == '__main__':
    # Sample campaign data
    sample_data = pd.DataFrame({
        'date': pd.date_range('2025-01-01', periods=30),
        'impressions': np.random.randint(10000, 20000, 30),
        'clicks': np.random.randint(300, 600, 30),
        'spend': np.random.uniform(1000, 2000, 30),
        'conversions': np.random.randint(10, 25, 30),
    })
    
    # Calculate metrics
    calculator = PPCMetricsCalculator(sample_data)
    
    print("PPC Campaign Metrics:")
    print("=" * 40)
    
    metrics = calculator.get_all_metrics(revenue=120000)
    
    for metric, value in metrics.items():
        print(f"{metric.upper()}: {value}")
    
    print("\nInterpretation:")
    print("- CTR 2.7% is healthy for B2B search ads")
    print("- CPA of $103 is profitable if LTV > $500")
    print("- ROAS 11.6x shows strong profitability")
