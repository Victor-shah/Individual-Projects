# End to End Industrial Quality & Sales Automation Pipeline

This project simulates a real-world scenario, that is, analyzing welding equipment data, predicting machinery maintenance needs, and automating internal workflows. 

[Insert flow chart]

Phase 1: Data Architecture (SQL)

We'll create a mock relational database representing a manufacturing plant using welding units.

Step 1: Create a database and populate with dummy data. Execute 'database_setup.py' to create a localize SQLite database file with realistic telemetry data. It simulates voltage spikes, overheating, and normal operations.

[insert the database created]

After the execution, 'factory.db' database is created. 

Phase 2: Predictive AI & Anomaly Detection (Python)

We query the SQL database and pass the raw features to an Isolation Forest Model. We use this model because its an industry-standard unsupervised machine learning model used extensively for sensor anomaly detection.

Step 1: Execute the 'anomaly_detector.py' to query the SQL database and pass the raw features to the unsupervised machine learning model. 

After the execution, we have a cleaned dataset 'output_insights.csv' ready to export for Power BI. Additionally, we prepared a lightweight structured JSON payload 'alerts_payload.json' for Power Automate. 

Phase 3: Executive Reporting (Power BI)

[insert the dashboard]
Review the insights

Phase 4: Digital Transformation (Power Automate Low-Code Integration)

Now we'll create a localized cloud trigger using Power Automate Desktop.

Step 1: Create a New flow by the name 'Factory_Alert_Pipeline'

Step 2: Drag and drop Action (Read text from file) to open and read the 'alerts_payload.json' file.

Step 3: Drag and drop Action (Convert JSON to custom object) to transform the file into a readable custom object. This helps to extract things like exact machine name and temperature. 

Step 4: We're left with the system alert notification. In this step we had a system pop-up box to simulate a factory control room dashboard alert. 

Step 5: We hit 'run' icon, and the alert box will pop up onto your screen.

[insert the working of this here]

Phase 5: Generative AI Prompt Engineering

This is the phase where we show how Copilot helps engineers troubleshoot failures. 

Step 1: Initialize the Agent, we name the agent [] and click create.

Step 2: We input the core instructions, which will prompt the agent to load an environment to work with.

Step 3: We test with the Telemetry Payload, and the Agent will generate the localized technical repair checklist. 

[insert the agent ss] 