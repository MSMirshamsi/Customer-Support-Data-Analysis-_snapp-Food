📋 Project Overview

This project analyzes customer support ticket data to uncover key factors affecting customer satisfaction (CSAT) and operational performance.

The goal is to demonstrate how data can be used for decision-making, process improvement, and strategic recommendations — reflecting real-world business analysis tasks.

🎯 Objectives

Identify patterns and relationships between service metrics (e.g., resolution time, SLA compliance) and customer satisfaction.

Evaluate how issue type, communication channel, and agent performance influence CSAT.

Provide actionable, data-driven recommendations to improve the overall support experience.

🧰 Tools & Technologies

Python 🐍

pandas, numpy → data cleaning & manipulation

matplotlib, seaborn → visualization

scipy.stats → statistical testing (Kruskal–Wallis, correlation)

sklearn → preprocessing, modeling

Excel → exploratory data validation and pivot summaries

Jupyter Notebook → analysis documentation and narrative

GitHub → version control and project presentation

📊 Dataset

The dataset consists of anonymized customer support tickets including:

Feature	Description
ticket_id	Unique ticket identifier
issue_type	Type of customer issue (billing, technical, cancellation, etc.)
channel	Communication channel (chat, email, phone)
response_time	Time to first response (minutes)
resolution_time	Total time to resolve issue (minutes)
sla_breached	Whether SLA was violated (0/1)
agent_id	Identifier for support agent
csat_score	Customer satisfaction rating (1–5)
🔍 Analytical Process

Data Cleaning & Preprocessing

Handled missing values and outliers.

Normalized time fields, standardized issue types, and encoded categorical variables.

Checked distribution and skewness to select appropriate statistical tests.

Exploratory Data Analysis (EDA)

Univariate and bivariate visualizations.

Distribution plots for response/resolution times.

Boxplots to compare CSAT across issue types and channels.

Statistical Analysis

Correlation analysis (Pearson, Spearman, Kendall) to understand linear and rank relationships between numeric variables.

Kruskal–Wallis H-test for non-parametric comparison across groups (issue type, channel).

SLA compliance analysis per agent and per issue type.

Insights Extraction

Insight 1️⃣: Relationship between resolution time and CSAT is weakly positive (r ≈ 0.13), suggesting time alone doesn’t determine satisfaction.

Insight 2️⃣: Issue type influences satisfaction — financial and cancellation issues yield lower CSAT, indicating process improvement opportunities.

Insight 3️⃣: Communication channel significantly affects satisfaction (p ≈ 0.04); chat leads to higher CSAT, while email underperforms.

Insight 4️⃣: SLA breach rate correlates negatively with satisfaction; ensuring SLA compliance is a key driver of customer happiness.

Visualization & Storytelling

Boxplots, heatmaps, and distribution charts to illustrate findings.

Focus on interpretable visual storytelling — turning data into actionable business insights.
