# 🧠 Customer Support Data Analysis Project
### Data-driven insights for improving customer satisfaction and service efficiency

---

## 📋 Project Overview
This project analyzes **customer support ticket data** to uncover key factors affecting **customer satisfaction (CSAT)** and **operational performance**.

The goal is to demonstrate how data can be used for **decision-making**, **process improvement**, and **strategic recommendations** — reflecting real-world business analytics tasks.

---

## 🎯 Objectives
- Identify relationships between operational metrics (response time, SLA compliance) and customer satisfaction.
- Evaluate how **issue type**, **communication channel**, and **agent performance** influence CSAT.
- Provide actionable, data-driven recommendations to improve service quality.

---

## 🧰 Tools & Technologies
- **Python** 🐍  
  `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `sklearn`
- **Excel** for validation and exploratory review
- **Jupyter Notebook** for documentation and EDA
- **GitHub** for version control and presentation

---

## 📊 Dataset
The dataset includes anonymized customer support tickets:

| Feature | Description |
|----------|-------------|
| `ticket_id` | Unique ticket identifier |
| `issue_type` | Type of issue (billing, technical, cancellation, etc.) |
| `channel` | Communication channel (chat, email, phone) |
| `response_time` | Time to first response (minutes) |
| `resolution_time` | Time to resolve issue (minutes) |
| `sla_breached` | SLA violation flag (0/1) |
| `agent_id` | Support agent identifier |
| `csat_score` | Customer satisfaction rating (1–5) |

---

## 🔍 Analytical Process

### 1. Data Cleaning & Preprocessing
- Handled missing values and outliers.
- Normalized time metrics and standardized categorical data.
- Checked distributions and skewness to choose proper statistical tests.

### 2. Exploratory Data Analysis (EDA)
- Univariate & bivariate visualizations.
- Boxplots to compare CSAT across **issue types** and **channels**.
- Heatmaps to identify correlations among variables.

### 3. Statistical Analysis
- **Correlation analysis (Pearson, Spearman, Kendall)** for numeric variables.
- **Kruskal–Wallis H-test** for non-parametric group comparison.
- **SLA compliance analysis** per agent and issue type.

### 4. Insights Extracted
- **Insight 1️⃣:** Weak positive correlation between **resolution time** and **CSAT** (r ≈ 0.13).  
- **Insight 2️⃣:** **Issue type** influences satisfaction — billing and cancellation issues show lower CSAT.  
- **Insight 3️⃣:** **Communication channel** significantly affects CSAT (p ≈ 0.04); chat leads to higher satisfaction.  
- **Insight 4️⃣:** **SLA breach rate** correlates negatively with CSAT; compliance drives satisfaction.  

### 5. Visualization & Storytelling
- Clear, intuitive charts (boxplots, histograms, heatmaps).
- Focused on translating data into actionable insights.

---

## 📈 Key Findings

| Category | Finding | Impact |
|-----------|----------|--------|
| ⏱️ Resolution Time | Weak correlation (r = 0.138) | Time alone not decisive |
| 💬 Issue Type | Billing & Cancellation lower CSAT | Requires process improvement |
| 📞 Channel | Chat > Phone > Email (p = 0.0396) | Channel optimization |
| ⚙️ SLA Compliance | Negative link with CSAT | Key operational KPI |
| 👩‍💼 Agent Variation | High variance | Needs targeted training |

---

## 💡 Recommendations
1. Prioritize **SLA compliance** — monitor and reduce breaches.  
2. Improve **financial and cancellation** workflows.  
3. Promote **chat** as the default support channel.  
4. Implement **targeted training** for underperforming agents.  
5. Build **feedback loops** and track performance KPIs continuously.  

---

## 🧮 Statistical Summary

| Test | Variable | Result | p-value | Interpretation |
|------|-----------|---------|---------|----------------|
| Pearson | CSAT vs Resolution Time | r = 0.138 | — | Weak positive |
| Kruskal–Wallis | CSAT vs Issue Type | H = 7.703 | 0.103 | Not significant |
| Kruskal–Wallis | CSAT vs Channel | H = 8.334 | 0.0396 | Significant difference |

---

## 🧠 Lessons & Skills Demonstrated
- Application of **data analytics for business decision support**
- Experience with **EDA, hypothesis testing, and correlation analysis**
- Ability to connect **statistical evidence with business context**
- **Data storytelling** through clear visuals and summaries
- Communicating insights to both **technical and business stakeholders**

---

## 📂 Repository Structure
