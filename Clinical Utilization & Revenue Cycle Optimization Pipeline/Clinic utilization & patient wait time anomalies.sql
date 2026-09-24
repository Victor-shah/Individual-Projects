-- Using PostgreSQL Window Functions (PARTITION BY) to compute local averages
SELECT 
    e.Encounter_ID,
    e.Clinic_Specialty,
    d.Gender,
    d.Nationality_Group,
    e.Waiting_Room_Minutes,
    -- Calculates the overall average wait time for that clinic specialty across all rows
    ROUND(AVG(e.Waiting_Room_Minutes) OVER(PARTITION BY e.Clinic_Specialty), 1) as Clinic_Average_Wait,
    -- Flags rows where the individual patient waited longer than their clinic's baseline average
    CASE 
        WHEN e.Waiting_Room_Minutes > AVG(e.Waiting_Room_Minutes) OVER(PARTITION BY e.Clinic_Specialty) THEN 'Above Average Delay'
        ELSE 'Normal Flow'
    END as Operational_Status
FROM fact_encounters e
JOIN dim_demographics d ON e.Patient_ID = d.Patient_ID
WHERE e.No_Show_Flag = 0; -- Only analyze patients who arrived
