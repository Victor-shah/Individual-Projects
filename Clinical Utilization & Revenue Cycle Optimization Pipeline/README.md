# End-to-End Clinical Utilization & Revenue Cycle Optimization Pipeline

This project simulates an operational challenge a multi-specialty clinic network faces, that is, predicting patient "no-shows", optimizing clinic utilization, and tracking revenue leakage from rejected insurance claims. 

[insert flowchart]

## Phase 1: Synthesize and Model Healthcare-Compliant Data (Python)

We'll be using healthcare domain standards, namely ICD-10, CPT, SNOMED CT and the raw "messiness" of live EHR. The EHR is the digital software system housing the entire patient chart. Inside that EHR, the doctor types notes, and SNOMED CT (for healthcare providers) runs in the background to log the exact clinical terms, symptoms, and anatomy automatically.

When the patient checks out, the EHR translates those clinical findings into an ICD-10 code (the diagnosis) and a CPT code (the procedure) so the billing department can submit a claim to the insurance company. 

**Step 1**: We write a python script '[synthesize_health_data.ipynb](synthesize_health_data.ipynb)' using libraries like pandas, numpy to generate a multi-table relational dataset representing HealthHub operations.

After executing the notebook, the following two schemas are built:

Encounter Table '[fact_encounters.csv](fact_encounters.csv)'
Encounter ID, Patient ID, Appointment Date/Time, Clinic Specialty, Waiting Room Time, a binary No_show flag. <div align = "center"> <h3> Encounter Table </h3>
<img width="962" height="222" alt="image" src="https://github.com/user-attachments/assets/40be59db-c627-4af4-b9f4-f3b371a460ef" /> </div>
<br>
<br>

Billing & Revenue Cycle (RCM) Table '[fact_billing.csv](fact_billing.csv)'
Transaction ID, Encounter ID, CPT Code, Gross Amount, Insurance Carrier, Claim Status, and Denial Reason Code. <div align ="center"> <h3> Billing & Revenue Cycle (RCM) Table </h3>
<img width="966" height="222" alt="image" src="https://github.com/user-attachments/assets/f32dcb04-c25a-4171-bec8-c71c66845ecc" /> </div>
<br>
<br>


**Step 2**: We write a python script '[normalize_health_data.ipynb](normalize_health_data.ipynb)' normalizing the created tables into separate tables to prevent redundancy. 

After executing the notebook, following schemas are built:

Demographics Table '[dim_demographics.csv](dim_demographics.csv)'
Patient ID, Age, Gender, Nationality, Emiratisation status, and Location <div align ="center"> <h3> Demographics Table </h3>
<img width="587" height="220" alt="image" src="https://github.com/user-attachments/assets/d73544d0-fda9-414c-b6be-9f1fb1310e8e" /> </div>
<br>
<br>


Clinical Diagnostics Table '[dim_diagnostics.csv](dim_diagnostics.csv)'
Encounter ID, ICD-10/11 Code (using SNOMED CT terms) <div align = "center"> <h3> Clinical Diagnostics Table </h3>
<img width="390" height="260" alt="image" src="https://github.com/user-attachments/assets/46479a9c-a71b-4f78-9677-5c0e7b2b76e7" /> </div>
<br>
<br>


## Phase 2: Establish a Production-Grade SQL Warehouse (PostgreSQL)

We will build a Star Schema Data Warehouse. In professional environments, databases are separated into Dimension tables and Fact tables. This design makes the data highly organized and allows visualization tools to query million-row databases instantly. 

**Step 1**: We run the following script '[]()' to create the data tables. We establish the relationships using PRIMARY KEY and FOREIGN KEY. 
<div align = "center"> <h3> Star Schema</h3>
<img width="1065" height="458" alt="image" src="https://github.com/user-attachments/assets/a6adf9c0-17e7-440c-b352-473a9a18af5c" /> </div>
<br>
<br>

**Step 2**: We import the CSV data from the excel files into PostgreSQL so that we can run queries on it. 

**Step 3**: Now that the data is live, we write queries using advanced concepts like Common Table Expressions (CTEs) and Window Functions. 

Query 1 --> Which clinic specialties are causing the highest rate of rejected insurance claims and how much money is trapped. [Revenue Leakage Report.sql](Revenue%20Leakage%20Report.sql)
<div align = "center"> <h3> Revenue Leakage Report</h3>
<img width="1141" height="207" alt="image" src="https://github.com/user-attachments/assets/0db8ac7e-329d-487f-b361-04567bff33f7" /> </div>
<br>
<br>


Query 2 --> Rank clinic wait times by demographic cohorts to discover operational bottlenecks. [Clinic utilization & patient wait time anomalies.sql](Clinic%20utilization%20&%20patient%20wait%20time%20anomalies.sql)
<div align = "center"> <h3>Clinic Utilization & Patient wait time anomalies</h3>
<img width="1318" height="202" alt="image" src="https://github.com/user-attachments/assets/a8f913b3-bfb0-41de-bf0e-372ae17c0969" /> </div>
<br>
<br>


## Phase 3: Engineer Predictive ML Models in Python

We can now transition from descriptive analytics to predictive analytics. Predicting an event before it happens saves enormous costs. Below are the applied machine learning models: 

Model 1: Patient No-show Prediction Engine

When a patient books an appointment but fails to show up, clinic utilization drops and an eligible patient loses their treatment slot. If we in advance knew that this patient had 85% probability of a No-Show, we could have overbook the slot safely. Below are the steps to execute this model:  

**Step 1**: We create a python script '[no_show_model.ipynb](no_show_model.ipynb)' that pulls live data from PostgreSQL, and applies feature engineering and trains an XGBoost Classifier. This classifier is favourable for structured tabular datasets. 
<div align = "center"> <h3> Model Performance Summary</h3>
<img width="551" height="218" alt="image" src="https://github.com/user-attachments/assets/a2f4c184-6337-4969-89c1-34a7386a58ce" /> </div>
<br> 
<br>

Key Insights
1. Precision for No-shows (Flag = 1): Measures out of all patients the model predicted would skip their appointment. 

2. Recall for No-shows (Flag = 1): Measures out of all patients who actually missed their appointments did our system catch. 

3. Feature importance weights. It identifies why patients miss slots. If **'Hour_of_Day'** turns out to have the highest weight, it gives the team the validation to change evening schedules.

Model 2: Claim Denial Risk Engine

When a claim is rejected by an insurance carrier (like Daman or AXA), the revenue cycle management (RCM) teams spend hours fixing it. If we build an engine that evaluates the combinations of CPT codes and ICD-10 codes to predict if a claim will be approved or rejected before it is sent to the insurance will save money. Below are the steps to execute this model:

**Step 1**: We create a python script '[rcm_denial_engine.ipynb](rcm_denial_engine.ipynb)' that pulls live data from PostgreSQL and applies feature engineering and trains an XGBoost Classifier. 
<div align = "center"> <h3>Model Performance Summary</h3>
<img width="541" height="296" alt="image" src="https://github.com/user-attachments/assets/9117ba0b-8561-4d43-9f82-509ce0648b3b" /> </div>
<br>
<br>


Key Insights
1. Precision for Rejected (Risk): Measures out of all insurance claims the model predicted would get their insurance rejected. 

2. Recall for Rejected (Risk): Measures out of all insurance claims who got rejeceted did our system catch. 

## Phase 4: Deploy the BI Dashboard Stack

Dashboard (Power BI) - Clinical Operations Tracker
<div align = "center"> <h3>Power BI Dashboard</h3>
<img width="752" height="645" alt="image" src="https://github.com/user-attachments/assets/c2137029-2b7e-4435-8a5f-889694f9f628" /> </div>
<br>
<br>

## Phase 5: Incorporate NABIDH and Local Compliance Documentation

Refer '[COMPLIANCE.md](COMPLIANCE.md)'
