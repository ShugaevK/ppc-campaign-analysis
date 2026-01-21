# PPC Campaign Analysis Case Study

## 📋 Project Overview

This repository contains a comprehensive analysis of a PPC (Pay-Per-Click) advertising campaign with a focus on performance metrics calculation, audience segmentation, and actionable optimization recommendations.

### Key Objectives:
- Calculate and analyze fundamental PPC metrics (CTR, CPC, CPA, ROAS)
- Perform cohort segmentation based on user acquisition channels
- Identify performance patterns and optimization opportunities
- Provide data-driven recommendations for campaign improvement

---

## 🎯 Campaign Brief

**Campaign Duration:** January 2025 - December 2025  
**Channels Analyzed:** Google Ads, Yandex Direct, VK Ads  
**Target Audience:** B2B SaaS buyers, 25-45 years old, Moscow region  
**Campaign Budget:** $50,000 USD  

---

## 📊 Dataset & Methodology

### Data Sources:
- Daily campaign performance from advertising platforms (impressions, clicks, conversions)
- Customer data: acquisition source, registration date, subscription status
- Revenue data: subscription plans, churn rate, lifetime value (LTV)

### Analysis Approach:
1. **Descriptive Analysis:** Campaign performance overview by channel and date
2. **Cohort Analysis:** User behavior grouped by acquisition month and channel
3. **Metrics Calculation:** CTR, CPC, CPA, ROAS, LTV, and payback period
4. **Trend Analysis:** Performance changes over time
5. **Segmentation:** High-value vs. low-value user cohorts

---

## 📈 Key Metrics Results

### Campaign Performance Summary

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Total Impressions** | 450,000 | Reach across all channels |
| **Total Clicks** | 12,150 | Overall engagement |
| **Overall CTR** | 2.7% | Within industry average (2-3%) |
| **Total Conversions** | 485 | Sign-ups from paid traffic |
| **Conversion Rate** | 3.99% | Strong conversion performance |
| **Total Spend** | $50,000 | Budget utilization |
| **Average CPC** | $4.11 | Cost per click across channels |
| **Average CPA** | $103.09 | Cost per acquisition |
| **Average Order Value (AOV)** | $2,400 | Avg annual subscription |
| **ROAS (Return on Ad Spend)** | 11.6x | $116 revenue per $1 spent |

### Channel Breakdown

| Channel | Impressions | Clicks | CTR | CPC | Conversions | CPA | ROAS |
|---------|------------|--------|-----|-----|-------------|-----|------|
| **Google Ads** | 250,000 | 7,500 | 3.0% | $3.80 | 320 | $95.31 | 13.2x |
| **Yandex Direct** | 150,000 | 3,600 | 2.4% | $4.50 | 110 | $136.36 | 8.8x |
| **VK Ads** | 50,000 | 1,050 | 2.1% | $5.20 | 55 | $151.82 | 6.3x |

**Insight:** Google Ads is the most efficient channel (highest ROAS, lowest CPA). VK Ads shows potential but needs optimization.

---

## 👥 Cohort Analysis Results

### Monthly Cohort Performance

| Cohort (Acq Month) | Users | Month 1 Retention | Month 3 Retention | LTV | Payback Period |
|--------------------|-------|-------------------|-------------------|-----|----------------|
| **January** | 45 | 91% | 78% | $2,850 | 1.3 months |
| **February** | 62 | 88% | 72% | $2,640 | 1.5 months |
| **March** | 58 | 90% | 75% | $2,760 | 1.4 months |
| **April-June (avg)** | 280 | 87% | 68% | $2,400 | 1.6 months |
| **July-September** | 200 | 84% | 61% | $2,100 | 1.9 months |
| **October-December** | 160 | 78% | 52% | $1,680 | 2.4 months |

**Key Finding:** Earlier cohorts show higher retention and LTV. Q4 users acquired later have higher churn rates.

### Channel Cohort Comparison

| Channel | Avg Retention (M3) | Avg LTV | User Quality Score |
|---------|-------------------|---------|--------------------|
| Google Ads | 74% | $2,750 | 8.5/10 |
| Yandex Direct | 68% | $2,350 | 7.2/10 |
| VK Ads | 62% | $2,100 | 6.8/10 |

---

## 💡 Key Insights & Findings

### Positive Findings:
1. **Strong ROAS:** 11.6x overall ROAS indicates highly profitable ad spend
2. **Good Conversion Rate:** 3.99% conversion rate is above B2B SaaS average (2-3%)
3. **Consistent Performance:** All channels deliver positive ROI
4. **High-Value Users:** Early cohorts (Jan-Mar) show strong LTV of $2,650+
5. **Efficient Payback:** Average 1.7-month payback period enables reinvestment

### Challenges Identified:
1. **Seasonal Decline:** Q4 user quality drops (lower retention, higher churn)
2. **Channel Quality Disparity:** VK Ads CPA is 59% higher than Google Ads
3. **Late-Stage Churn:** Users acquired in Q4 show only 52% M3 retention
4. **CPC Escalation:** Yandex Direct CPC rising over time (+12% from Jan to Dec)
5. **Channel Saturation:** CTR declining in Google Ads (3.2% Jan → 2.8% Dec)

---

## 🔧 Optimization Recommendations

### Immediate Actions (Weeks 1-2):
1. **Pause underperforming VK Ads campaigns** with CPA > $200
   - Expected impact: +5-8% overall ROAS
   - Action: Review creative quality and landing page experience

2. **Reallocate 30% of VK budget to Google Ads**
   - Expected impact: -15-20% blended CPA
   - Reason: Google Ads shows 2.1x better efficiency

3. **Audit Q4 landing pages**
   - High churn in late cohorts suggests UX/onboarding issues
   - Test: Simplify onboarding, improve first-login experience

### Medium-Term Optimization (Months 2-3):
4. **Implement audience segmentation in Google Ads**
   - Target high-LTV profile (professionals, 30-45 age, decision-makers)
   - Expected: +8-12% conversion rate on new audiences

5. **Run A/B tests on ad copy focusing on retention signals**
   - Test messaging around "90%+ user retention," "enterprise support"
   - Target early cohort messaging to match higher-LTV patterns

6. **Yandex Direct optimization**
   - Reduce bids on low-converting keywords (CPA > $150)
   - Expected: +6-10% efficiency improvement

### Strategic Initiatives (3-6 months):
7. **Develop seasonal campaigns**
   - Q4 challenges suggest need for different positioning (e.g., "year-end planning tool")
   - Create 2-3 seasonal variations of landing pages

8. **Implement early engagement program**
   - 30-day post-signup nurture sequence
   - Target: Increase M3 retention by 5-8%

9. **Cohort-based retargeting**
   - Reactivate at-risk users from Q4 cohorts before churn
   - Budget: 10% of current ad spend

---

## 📁 Project Files

```
.
├── data/
│   ├── campaign_data.csv          # Daily metrics by channel (impressions, clicks, spend)
│   ├── conversion_data.csv        # User conversions and registration details
│   └── revenue_data.csv           # Subscription data, churn, LTV calculations
├── analysis/
│   ├── metrics_calculation.py     # CTR, CPC, CPA, ROAS calculations
│   ├── cohort_analysis.py         # Monthly cohort segmentation & retention
│   └── channel_comparison.py      # Channel performance breakdown
├── results/
│   ├── campaign_summary.xlsx      # Executive summary dashboard
│   ├── cohort_retention.xlsx      # Retention curves by cohort
│   └── visualizations/            # Charts and graphs
│       ├── channel_roas.png
│       ├── cohort_retention_curve.png
│       └── cpa_trend.png
└── README.md                       # This file
```

---

## 🛠 Tools & Technologies Used

- **Python 3.9+** - Data processing and analysis
- **Pandas** - Data manipulation and cohort analysis
- **NumPy** - Numerical calculations
- **Matplotlib / Seaborn** - Data visualization
- **Excel / Google Sheets** - Summary dashboards
- **SQL** - Data querying from analytics platforms

---

## 📌 Key Takeaways for Performance Marketers

1. **Metric Mastery:** Understanding CTR, CPC, CPA, and ROAS is fundamental to campaign optimization
2. **Cohort Thinking:** Segment users by acquisition source and time to identify quality differences
3. **Channel Efficiency:** Not all traffic is equal—VK Ads costs 59% more per acquisition
4. **Payback Period:** Quick payback (1.7 months) enables aggressive reinvestment and scaling
5. **Early Indicators:** Retention trends in first 30 days predict long-term LTV
6. **Data-Driven Decisions:** Use cohort data to inform budget allocation and creative strategy

---

## 📞 Contact & Questions

For questions about this analysis or methodology, feel free to open an issue or contact the author.

**Performance Marketing Focus Areas:**
- PPC Campaign Optimization
- Cohort & Retention Analysis
- ROAS Maximization
- Marketing Analytics

---

**Last Updated:** January 2026  
**Analysis Period:** Q1 2025 - Q4 2025
