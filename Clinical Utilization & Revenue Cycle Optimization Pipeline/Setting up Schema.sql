-- 1. Create Dimensions (Lookup Tables First)
CREATE TABLE dim_demographics (
    Patient_ID VARCHAR(50) PRIMARY KEY,
    Age INT,
    Gender VARCHAR(10),
    Nationality_Group VARCHAR(50),
    Primary_Clinic_Location VARCHAR(100)
);

CREATE TABLE dim_diagnostics (
    ICD10_Code VARCHAR(20) PRIMARY KEY,
    SNOMED_Description VARCHAR(250)
);

-- 2. Create Fact Tables (Transactions that point to Dimensions)
CREATE TABLE fact_encounters (
    Encounter_ID VARCHAR(50) PRIMARY KEY,
    Patient_ID VARCHAR(50) REFERENCES dim_demographics(Patient_ID),
    Appointment_DateTime TIMESTAMP,
    Clinic_Specialty VARCHAR(100),
    Waiting_Room_Minutes INT,
    ICD10_Code VARCHAR(20) REFERENCES dim_diagnostics(ICD10_Code),
    No_Show_Flag INT
);

CREATE TABLE fact_billing (
    Transaction_ID VARCHAR(50) PRIMARY KEY,
    Encounter_ID VARCHAR(50) REFERENCES fact_encounters(Encounter_ID),
    CPT_Code VARCHAR(20),
    Insurance_Carrier VARCHAR(100),
    Gross_Amount_AED NUMERIC(10, 2),
    Claim_Status VARCHAR(20),
    Denial_Reason VARCHAR(150)
);
