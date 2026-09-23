# Smart Metro Operation Analytics & Policy Evaluation System

An advanced data analytics, forecasting, and policy evaluation framework designed for urban metro transit networks (benchmarked on the **Delhi Metro** system). This project processes complex operational datasets to deliver interactive visual dashboards, multi-variable time series forecasts, dynamic pricing simulations, and data-driven risk assessment frameworks.

## Project Overview

Modern metro networks generate vast amounts of data across various operational parameters. This repository contains a comprehensive pipeline that transforms raw transactional and trip datasets into high-utility strategic insights. 

The analytical workflow transitions from foundational data cleansing and Exploratory Data Analysis (EDA) to rigorous statistical modeling (ARIMA/SARIMA/VAR), culminating in an actionable framework for policy deployment and revenue optimization.

---

## Key Features & Pipeline Architecture

### 1. Data Cleaning & Feature Engineering
* **Data Ingestion:** Standardizes schema formats containing variables like distances, fares, passenger volumes, and event remarks.
* **Temporal Parsing:** Transforms calendar dates into structured indices, extracting chronological dimensions (`Year`, `Month`, `Day`, `DayOfWeek`, `MonthYear`).
* **Feature Extraction:** Dynamically calculates micro-metrics such as `Total_Revenue` (`Fare` × `Passengers`).

### 2. Exploratory Data Analysis (EDA) & Centrality Reporting
* **Distribution Histograms:** Evaluates traffic volume, distance spreads, operational cost segments, and financial yield distributions.
* **Station Network Analysis:** Examines structural network hubs by checking centrality metrics, net commuter inflows/outflows, and volume tiers (Hubs vs. Major vs. Minor).
* **Segment Profiling:** Classes commuter volumes into behavioral segments (`Small`, `Medium`, `Large`, `Very Large`).

### 3. Predictive Modeling & Time Series Forecasting
* **Stationarity & Decomposition:** Integrates Augmented Dickey-Fuller (ADF) checks alongside additive structural trends, seasonality, and residual noise extractions.
* **Univariate Modeling:** Trains configurations of standard AutoRegressive Integrated Moving Average (`ARIMA`) and Seasonal ARIMA (`SARIMA`) networks to isolate optimal configurations.
* **Multivariate Vector Auto-Regression (`VAR`):** Captures multi-variable cross-correlations by simultaneously forecasting passenger throughput, target frequencies, and top line revenues.
* **Residual Analysis:** Evaluates forecasting validity with automated Ljung-Box test diagnostics, Q-Q plots, and Auto-Correlation Function (ACF) distribution bars.

### 4. Policy Evaluation & Revenue Optimization Simulation
* **Fare Elasticity Engine:** Simulates financial shifts against hypothetical pricing adjustments using standardized economic demand elasticity thresholds.
* **Peak vs. Off-Peak Analysis:** Assesses infrastructure margins under varying time-based pressures, identifying opportunities for smart dynamic pricing upgrades.
* **Strategic Roadmap Builder:** Assembles explicit 12-month policy implementations categorized by immediacy, resource commitment, ROI, and localized risk margins.

---

## Technology Stack & Dependencies

The complete ecosystem is built entirely within an optimized Python environment using major data science libraries:

* **Core Processing:** `pandas`, `numpy`, `scipy`
* **Data Visualization:** `plotly` (Express, Graph Objects, and Subplots)
* **Statistical Modeling:** `statsmodels` (ADF, Seasonal Decompose, VAR)
* **Machine Learning:** `scikit-learn` (Metrics framework)

---

## Repository Structure

```text
├── Smart Metro Operation Analytics System Dataset.csv  # Operational source metrics
├── Smart-Metro-Operation-Analytics.ipynb               # Primary notebook pipeline 
└── README.md                                           # System documentation
```

---

## Strategic Insights & Strategic Roadmap

The model generates automated strategic markers to inform transit authority decisions:

### 1. Operational Discoveries
* Identifies clear demand variations across travel paths, filtering out top-tier core hub networks from underperforming local zones.
* Pinpoints revenue capture trends differentiated across consumer pass types (`Smart Card`, `Tourist Card`, `Single Journey Ticket`).

### 2. Implementation Roadmap
* **Immediate (0-3 Months):** Launch smart dynamic peak premiums (+25% over base fare structures) to better balance traffic density.
* **Medium-Term (3-12 Months):** Release structural frequency scaling across high-revenue corridors alongside incentive-backed Smart Card loyalty schemas.
* **Long-Term (12+ Months):** Migrate data outputs towards digital integrations, embedding AI-powered capacity trackers and smart app booking frameworks.

---

## Quick Start & Installation

To run this analytics system locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd Individual-Projects/Smart-Metro-Operation-Analytics-System-main
   ```

2. **Install the required packages:**
   ```bash
   pip install pandas numpy plotly statsmodels scikit-learn scipy
   ```

3. **Launch the processing environment:**
   ```bash
   jupyter notebook
   ```
   Open `Smart-Metro-Operation-Analytics.ipynb` and execute all cells to reproduce the dashboards and forecasting models.
