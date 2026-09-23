# End to End Industrial Quality & Sales Automation Pipeline

This project simulates a real-world scenario, that is, analyzing welding equipment data, predicting machinery maintenance needs, and automating internal workflows. 

Below is the flowchart, and the step by step procedure to go through this project.

<img width="757" height="581" alt="image" src="https://github.com/user-attachments/assets/fb403909-43bd-4006-8bf0-feb60437745d" />


## Phase 1: Data Architecture (SQL)

We'll create a mock relational database representing a manufacturing plant using welding units.

**Step 1**: Create a database and populate with dummy data. Execute '[database_setup.ipynb](database_setup.ipynb)' to create a localize SQLite database file with realistic telemetry data. It simulates voltage spikes, overheating, and normal operations.

Below is the schema of the database. 

<img width="978" height="150" alt="image" src="https://github.com/user-attachments/assets/12aa554a-1b28-4372-b6ff-d86116b4dacf" />


After the execution, '[factory.db](factory.db)' database is created. 

## Phase 2: Predictive AI & Anomaly Detection (Python)

We query the SQL database and pass the raw features to an Isolation Forest Model. We use this model because its an industry-standard unsupervised machine learning model used extensively for sensor anomaly detection.

**Step 1**: Execute the '[anomaly_detector.ipynb](anomaly_detector.ipynb)' to query the SQL database and pass the raw features to the unsupervised machine learning model. 

After the execution, we have a cleaned dataset 'output_insights.csv' ready to export for Power BI. Additionally, we prepared a lightweight structured JSON payload '[alerts_payload.json](alerts_payload.json)' for Power Automate. 

## Phase 3: Executive Reporting (Power BI)

<img width="1157" height="638" alt="image" src="https://github.com/user-attachments/assets/6726407d-0f0d-48ea-abd7-a6efbfef72c9" />


**Key Findings**
1. There are a total of 3 operational machines.
2. Out of 10,000 records 87 alerts were raised.
3. The donut chart provides a visual breakdown of how much of the factory equipment is running safely versus how much needs immediate attention. 
4. The line chart lets managers look back in time to see exactly 'when' an anomaly occurred and how voltage or temperature behaved leading up to the failure.

## Phase 4: Digital Transformation (Power Automate Low-Code Integration)

Now we'll create a localized cloud trigger using Power Automate Desktop.

**Step 1**: Create a New flow by the name 'Factory_Alert_Pipeline'

**Step 2**: Drag and drop Action (Read text from file) to open and read the 'alerts_payload.json' file.

**Step 3**: Drag and drop Action (Convert JSON to custom object) to transform the file into a readable custom object. This helps to extract things like exact machine name and temperature. 

**Step 4**: We're left with the system alert notification. In this step we had a system pop-up box to simulate a factory control room dashboard alert. 

**Step 5**: We hit 'run' icon, and the alert box will pop up onto your screen.

Below is the workflow for Power Automate.

<img width="787" height="891" alt="Screenshot 2026-09-23 150202" src="https://github.com/user-attachments/assets/8990d9e3-1af4-467c-b6ea-e9509b28a63b" />


## Phase 5: Generative AI Prompt Engineering

This is the phase where we show how Copilot helps engineers troubleshoot failures. 

**Step 1**: Initialize the Agent, we name the agent 'Field Troubleshooter' and click create.

**Step 2**: We input the core instructions, which will prompt the agent to load an environment to work with.

**Step 3**: We test with the Telemetry Payload, and the Agent will generate the localized technical repair checklist. 

Below is the Custom created Agent overview.

<img width="1640" height="898" alt="Screenshot 2026-09-23 152648" src="https://github.com/user-attachments/assets/b144ebba-9321-4ca4-aac1-fe1f2a955c97" />
