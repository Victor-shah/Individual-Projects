# End-to-End Clinical Utilization & Revenue Cycle Optimization Pipeline

This project simulates an operational challenge a multi-specialty clinic network faces, that is, predicting patient "no-shows", optimizing clinic utilization, and tracking revenue leakage from rejected insurance claims. 

[insert flowchart]

## Phase 1: Synthesize and Model Healthcare-Compliant Data (Python)

We'll be using healthcare domain standards, namely ICD-10, CPT, SNOMED CT and the raw "messiness" of live EHR. The EHR is the digital software system housing the entire patient chart. Inside that EHR, the doctor types notes, and SNOMED CT (for healthcare providers) runs in the background to log the exact clinical terms, symptoms, and anatomy automatically.

When the patient checks out, the EHR translates those clinical findings into an ICD-10 code (the diagnosis) and a CPT code (the procedure) so the billing department can submit a claim to the insurance company. 

**Step 1**: We write a python script '[synthesize_health_data.ipynb](synthesize_health_data.ipynb)' using libraries like pandas, numpy to generate a multi-table relational dataset representing HealthHub operations.

After executing the notebook, the following two schemas are built:

Encounter Table '[fact_encounters.csv](fact_encounters.csv)'
Encounter ID, Patient ID, Appointment Date/Time, Clinic Specialty, Waiting Room Time, a binary No_show flag
[insert table]

Billing & Revenue Cycle (RCM) Table '[fact_billing.csv](fact_billing.csv)'
Transaction ID, Encounter ID, CPT Code, Gross Amount, Insurance Carrier, Claim Status, and Denial Reason Code. 
[insert table]

**Step 2**: We write a python script '[normalize_health_data.ipynb](normalize_health_data.ipynb)' normalizing the created tables into separate tables to prevent redundancy. 

After executing the notebook, following schemas are built:

Demographics Table '[dim_demographics.csv](dim_demographics.csv)'
Patient ID, Age, Gender, Nationality, Emiratisation status, and Location
[insert table]

Clinical Diagnostics Table '[dim_diagnostics.csv](dim_diagnostics.csv)'
Encounter ID, ICD-10/11 Code (using SNOMED CT terms)
[insert table]

## Phase 2: Establish a Production-Grade SQL Warehouse (PostgreSQL)

We will build a Star Schema Data Warehouse. In professional environments, databases are separated into Dimension tables and Fact tables. This design makes the data highly organized and allows visualization tools to query million-row databases instantly. 

**Step 1**: We run the following script '[]()' to create the data tables. We establish the relationships using PRIMARY KEY an FOREIGN KEY. 

[insert star schema]

**Step 2**: We import the CSV data from the excel files into PostgreSQL so that we can run queries on it. 

**Step 3**: Now that the data is live, we write queries using advanced concepts like Common Table Expressions (CTEs) and Window Functions. 

Query 1 --> Which clinic specialties are causing the highest rate of rejected insurance claims and how much money is trapped. [.sql]()

[insert o/p here]

Query 2 --> Rank clinic wait times by demographic cohorts to discover operational bottlenecks. [.sql]()

[insert o/p here]

## Phase 3: Engineer Predictive ML Models in Python

We can now transition from descriptive analytics to predictive analytics. Predicting an event before it happens saves enormous costs. Below are the applied machine learning models: 

Model 1: Patient No-show Prediction Engine

When a patient books an appointment but fails to show up, clinic utilization drops and an eligible patient loses their treatment slot. If we in advance knew that this patient had 85% probability of a No-Show, we could have overbook the slot safely. Below are the steps to execute this model:  

**Step 1**: We create a python script '[no_show_model.ipynb](no_show_model.ipynb)' that pulls live data from PostgreSQL, and applies feature engineering and trains an XGBoost Classifier. This classifier is favourable for structured tabular datasets. 

[insert the model performance summary]

Key Insights
1. Precision for No-shows (Flag = 1): Measures out of all patients the model predicted would skip their appointment. 

2. Recall for No-shows (Flag = 1): Measures out of all patients who actually missed their appointments did our system catch. 

3. Feature importance weights. It identifies why patients miss slots. If **'Hour_of_Day'** turns out to have the highest weight, it gives the team the validation to change evening schedules.

Model 2: Claim Denial Risk Engine

When a claim is rejected by an insurance carrier (like Daman or AXA), the revenue cycle management (RCM) teams spend hours fixing it. If we build an engine that evaluates the combinations of CPT codes and ICD-10 codes to predict if a claim will be approved or rejected before it is sent to the insurance will save money. Below are the steps to execute this model:

**Step 1**: We create a python script '[rcm_denial_engine.ipynb](rcm_denial_engine.ipynb)' that pulls live data from PostgreSQL and applies feature engineering and trains an XGBoost Classifier. 

[insert the model performance summary]

Key Insights
1. Precision for Rejected (Risk): Measures out of all insurance claims the model predicted would get their insurance rejected. 

2. Recall for Rejected (Risk): Measures out of all insurance claims who got rejeceted did our system catch. 

## Phase 4: Deploy the Dual BI Dashboard Stack

Dashboard A (Power BI) - Clinical Operations Tracker

[insert dashboard here]

Dashboard B (Tableau) - Executive RCM & Finance Summary

[insert dashboard here]

## Phase 5: Incorporate NABIDH and Local Compliance Documentation