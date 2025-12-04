# 📈 Page View Time Series Visualizer

### 🚀 Project Overview
This project visualizes time series data using **Python**, **Pandas**, **Matplotlib**, and **Seaborn**. It analyzes the daily page view traffic of the freeCodeCamp.org forum from 2016 to 2019, identifying growth trends and seasonal patterns.

**Key Objective:** Clean raw time-series data, handle date indexing, and generate production-grade charts to communicate user engagement insights.

### 📊 Visualizations Generated
This project creates three specific types of time-series visualizations:

#### 1. Line Chart (Growth Trend)
* **Technique:** Matplotlib Line Plot.
* **Insight:** Visualizes the overall daily traffic growth from May 2016 to December 2019.
* **Feature:** Filters out the top and bottom 2.5% of data outliers to clean the noise.

#### 2. Bar Chart (Yearly & Monthly Growth)
* **Technique:** Grouped Bar Chart (Pandas `groupby` & `unstack`).
* **Insight:** Shows average daily page views for each month, grouped by year.
* **Key Skill:** Custom categorical sorting to ensure months appear in calendar order (Jan -> Dec), not alphabetical order.

#### 3. Box Plots (Seasonality & Trend)
* **Technique:** Seaborn Box Plots (`sns.boxplot`).
* **Insight:**
    * **Year-wise:** Displays the spread and median of traffic for each year.
    * **Month-wise:** Reveals seasonal patterns (e.g., traffic spikes in specific months) and distribution spread.

### 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Manipulation:** Pandas (Time Series Indexing, Quantile Filtering, Grouping)
* **Visualization:** Matplotlib, Seaborn
* **Data Cleaning:** Outlier removal (Top/Bottom 2.5% quantile filtering)

### 📂 Project Structure
* `time_series_visualizer.py`: The main script containing the visualization logic.
* `main.py`: Entry point for running the analysis.
* `test_module.py`: Unit tests to verify chart accuracy.
* `fcc-forum-pageviews.csv`: The raw dataset.

### 🏆 Certification
This project is part of the **FreeCodeCamp Data Analysis with Python Certification**.
