Following is the step by step data preparation and cleaning procedure using MS Excel.

Step 1: Downloaded the dataset (.csv) and created a table. The given dataset is structured properly representing the states of the US. 

Step 2: To convert this dataset to fit the GCC region, we'll have to use the "XLOOKUP" function. We insert two new columns, "GCC City, GCC Country" that will be derived from the current column "State". 

Step 3: Created a separate sheet "Mapping" for filling the values of the newly created columns using the "XLOOKUP" function.  

Step 4: After filling the values in the newly created columns and paste them as values, we delete the "State" column.

Step 2,3,4 involved localize the data. 

Step 5: Checking for missing values in the sheet. We check for missing values to prevent broken formulas and distorted metrics. 

Step 6: Standardize your financial formats. We'll have to check the "Sales, Revenue and Profit" columns if they contain any mixed text and numbers. 

Step 7: Validate and Unify Date formatting. Sometimes dates are formatted differently which would lead to Pivot tables to break. 

Step 5,6,7 involved cleaning the data.

Step 8: Creating a "Targets" Sheet, and we assign each city's target in the main sheet using "XLOOKUP" function.

Step 9: Building a "Master KPIs" Summary Grid
a) Total UAE/GCC Revenue
b) Target Variance Percentage
c) High-Volume Transaction Count

Step 10: An "Alert List" of low-performing transactions
