# College Majors, Salary, and Career Meaningfulness Analysis
##  Objective

The objective of this project is to explore the relationship between salary outcomes and perceived career meaningfulness across a wide range of college majors. By analyzing early and mid-career salary data alongside survey-based meaningfulness ratings, this project aims to determine whether financially lucrative careers tend to align with higher levels of reported career satisfaction — or whether a trade-off exists between monetary reward and purpose-driven work.

This analysis is conducted using Python, with tools including pandas, matplotlib, seaborn, and scikit-learn for data cleaning, statistical analysis, visualization, and linear regression modeling.

## Hypothesis
I believe there is a positive correlation between higher-earning careers and the perceived meaningfulness of those careers.

My reasoning is that people who are well-compensated are more likely to feel satisfied and, as a result, find greater meaning in their work. I expect the highest earners to primarily come from STEM or STEM-adjacent fields (e.g., Engineering, Computer Science, Economics), while lower earners will likely be concentrated in the humanities or creative arts.

If this hypothesis is incorrect, it may suggest a trade-off between financial reward and perceived meaning in one’s career.

---

## Methodology

### Data Cleaning
- Removed currency symbols and percent signs from key columns.
- Converted relevant columns to numeric types to ensure accurate statistical computation.

### Summary Statistics
- Calculated quantiles (1st percentile, 25th, median, 75th, 99th) for:
  - Early Career Pay
  - Mid-Career Pay
  - % High Meaning

### Statistical Measures
- Computed average and standard deviation for both Early and Mid-Career salaries.

### Categorization
- Grouped majors into broader categories:
  - STEM
  - Business
  - Arts
  - Education
  - Social Sciences
  - Other

---

## Visualizations

### 1. Line Plots
- **Early Career Pay w/ Deviation**
- **Mid Career Pay w/ Deviation**

### 2. Regression Analysis
- Scatter plot of % High Meaning vs Mid-Career Pay
- Linear regression line overlay
- R² value printed to assess model fit

### 3. Heatmap
- Correlation matrix visualized using seaborn

### 4. Pie Chart
- Distribution of majors by category

---

## Exploratory Data Insights

### High Meaning + High Pay ("Best Careers")
Majors with >63% high meaning and >$115,400 mid-career pay.

### Low Meaning + High Pay ("Trade-off Careers")
Majors with <44% high meaning and >$115,400 mid-career pay.

### High Meaning + Low Pay
Majors with >63% high meaning and <$83,750 mid-career pay.

### Low Meaning + Low Pay ("Avoid")
Majors with <44% high meaning and <$83,750 mid-career pay.

---

## Category Summary Table
- Aggregated by category using `groupby`.
- Reported average Mid-Career Pay and % High Meaning.

---

## Key Metrics
- R² value for regression between % High Meaning and Mid-Career Pay
- Average ranks of top/bottom 25 meaningful majors
- Null value counts for each column

---

## Conclusion
The analysis did not fully support the initial hypothesis. Contrary to expectations, the data shows a slightly **negative correlation** between mid-career salaries and the percentage of individuals who report finding high meaning in their work.

This suggests that **higher financial compensation does not necessarily align with perceived purpose** or fulfillment. STEM and finance-oriented majors still dominate the high-paying landscape.

There is more variance in early-career salaries than mid-career salaries. This is likely due to limited wage negotiation power early in one's career. The upper range is unconstrained, but entry-level positions cluster due to wage floors.

Interestingly, people report higher meaning early in their careers. Possibly due to hands-on involvement, while experienced professionals may feel more distanced from impactful tasks due to role changes.

In sum, the data suggests a nuanced relationship between **money and meaning**. While some careers offer both, others require a trade-off. Quantitative analysis, visualizations, and categorization helped highlight these insights.

---

## Appendix

### Top 25 Highest Mid-Career Salaries
*(Table printed via script)*

### Top 25 Lowest Mid-Career Salaries
*(Table printed via script)*

### Top 25 Highest % High Meaning Majors
*(Table printed via script)*

### Top 25 Lowest % High Meaning Majors
*(Table printed via script)*

## Data Source
https://www.kaggle.com/datasets/rathoddharmendra/post-college-salaries
