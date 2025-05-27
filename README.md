# 🎓 Career Meaning vs. Salary Analysis

## 📌 Objective

To explore the relationship between **mid-career salaries** and the **perceived meaningfulness** of various college majors. The goal is to identify:
- Whether highly paid careers are also meaningful
- Which majors offer the best trade-off between compensation and meaning
- Which fields may lack both

---

## 🧠 Hypothesis

> I believe there is a positive correlation between higher-earning careers and the perceived meaningfulness of those careers.

People who are well-compensated are more likely to feel satisfied and, as a result, find greater meaning in their work. I expect the highest earners to primarily come from STEM or finance-adjacent fields, while the lowest earners will likely be in the humanities or creative arts. If this hypothesis is incorrect, it may suggest a trade-off between financial reward and perceived meaning.

---

## 🧹 Data Cleaning

- Removed `$`, `,`, and `%` from numeric columns.
- Converted columns like `Mid-Career Pay` and `% High Meaning` to numeric types.
- Created a new column `Category` by manually classifying majors into groups such as `STEM`, `Business`, `Arts`, etc.
- Dropped rows with missing values in critical columns like `% High Meaning`.

> ✅ **Missing Values Summary**  
> `% High Meaning`: 55 missing rows (dropped from analysis)

---

## 📊 Key Statistics

**Mid-Career Pay Quantiles**
0.01 $56,748
0.25 $83,750
0.50 $97,400
0.75 $115,400
0.99 $165,594

markdown
Copy

**% High Meaning Quantiles**
0.01 27%
0.25 44%
0.50 52%
0.75 63%
0.99 86.93%

yaml
Copy

---

## 📈 Visualizations

- **Error bar plots** of early and mid-career salary data
- **Linear regression** between `% High Meaning` and `Mid-Career Pay`
- **Heatmap** of correlations among salary and meaningfulness metrics

---

## 🧠 Insights

- **Correlation between % High Meaning and Mid-Career Pay**: `-0.262`  
  → Suggests a **slight inverse relationship** between pay and meaning.
  
- **Average Rank of Top 25 High-Meaning Majors**: `532.84`  
- **Average Rank of Bottom 25 High-Meaning Majors**: `331.92`

---

## 🎯 Career Segments

| Segment                                 | Criteria                                           |
|----------------------------------------|----------------------------------------------------|
| **Best Careers**                       | > 63% meaning & > $115,400 mid-career pay         |
| **Trade-offs (Money but not Meaning)** | < 44% meaning & > $115,400 mid-career pay         |
| **Meaningful but Low Pay**             | > 63% meaning & < $83,750 mid-career pay          |
| **Avoid (Low Pay + Low Meaning)**      | < 44% meaning & < $83,750 mid-career pay          |

---

## 📌 Conclusion

- Contrary to expectations, **high pay does not strongly correlate with meaningfulness**.
- **STEM and finance-related majors** offer the highest mid-career earnings, but often at the cost of lower perceived purpose.
- Many **health, education, and social work** majors report high levels of meaning despite lower salaries.
- Variance in **early-career pay** is higher due to wage floors and career uncertainty.
- The data supports the idea of a **meaning vs. money trade-off** in many career paths.

---

## 🛠️ Tools Used

- **Python**, **Pandas**, **Matplotlib**, **Seaborn**
- `LinearRegression` from **scikit-learn**

---

## 📁 Appendix

Includes raw tables of:
- Top 25 highest-earning majors
- Top 25 lowest-earning majors
- Top 25 highest and lowest satisfaction majors
