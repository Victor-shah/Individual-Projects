-- Use a CTE (WITH clause) to isolate financial aggregations first
WITH FinancialSummary AS (
    SELECT 
        e.Clinic_Specialty,
        COUNT(b.Transaction_ID) as Total_Claims,
        SUM(b.Gross_Amount_AED) as Total_Gross_Revenue,
        SUM(CASE WHEN b.Claim_Status = 'Rejected' THEN b.Gross_Amount_AED ELSE 0 END) as Denied_Revenue,
        SUM(CASE WHEN b.Claim_Status = 'Rejected' THEN 1 ELSE 0 END) as Total_Denials
    FROM fact_billing b
    JOIN fact_encounters e ON b.Encounter_ID = e.Encounter_ID
    GROUP BY e.Clinic_Specialty
)
-- Main select statement calculating percentages
SELECT 
    Clinic_Specialty,
    Total_Claims,
    Total_Gross_Revenue,
    Denied_Revenue,
    ROUND((Total_Denials::NUMERIC / Total_Claims) * 100, 2) as Claims_Denial_Rate_Percentage,
    ROUND((Denied_Revenue / Total_Gross_Revenue) * 100, 2) as Value_Leakage_Percentage
FROM FinancialSummary
ORDER BY Denied_Revenue DESC;
