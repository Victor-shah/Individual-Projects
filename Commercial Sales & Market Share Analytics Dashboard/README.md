# GCC Regional Sales Dataset & Guide

A comprehensive dataset detailing sales transactions across major **GCC (Gulf Cooperation Council) cities and countries** from **2014 to 2017**. This document outlines the file layout, data definitions, and step-by-step procedures to replicate or update the workbook's built-in analytical tables and dashboards.

---

## Sheet Structure & Content

The workbook is systematically split into logical sections or individual sheets containing structural indices and operational tables:

*   **Transactional Ledger:** Contains raw retail transaction records with details on order dates, geographical paths, categorizations, and monetary valuations.
*   **Sales Dashboard Tables:** Aggregated summary matrices breaking down total revenue, customer metrics, performance over time, and geographic distribution.
*   **Geographic Reference Mapping:** A reference matrix mapping standard US States to corresponding localized target GCC Cities (e.g., Texas ➔ Dubai, UAE).

---

## Data Dictionary & Column Definitions

The data ledger relies on the following columns located within the main transactional data template:

| Column Name | Data Type | Description / Values |
| :--- | :--- | :--- |
| **Order Date** | *Date* | Format: `YYYY-MM-DD`. Spans sequentially from 2014-01-03 to 2017-12-31. |
| **Customer Name** | *Text* | Unique identifier of the purchasing individual or corporate account entity. |
| **GCC Cities** | *Dropdown* | Fixed regional hubs: `Dubai`, `Abu Dhabi`, `Sharjah`, `Riyadh`, `Doha`, `Muscat`. |
| **GCC Countries** | *Dropdown* | Nation representing the city destination: `UAE`, `Saudi Arabia`, `Qatar`, `Oman`. |
| **Category** | *Dropdown* | High-level division: `Furniture`, `Office Supplies`, `Technology`. |
| **Sub-Category** | *Dropdown* | Detailed product groups (e.g., `Chairs`, `Paper`, `Phones`, `Appliances`). |
| **Product Name** | *Text* | Manufacturer item code, design variant, or specific commercial descriptor. |
| **Sales** | *Currency* | Gross revenue value ledger track for the item lines sold. |
| **Quantity** | *Integer* | Total item volume units counted within the line transaction segment. |
| **Profit** | *Currency* | Net margins. Negative formatting represents distinct baseline segment losses. |

---

## Step-by-Step Analytical Procedures

Follow these procedures to accurately reconstruct, modify, or extend the summarized dashboard layout from the transactional log entries:

### Procedure 1: Replicate Category & Sub-Category Sales Rank
1. select the complete tabular block containing transactional rows from **Order Date** down to **Profit**.
2. Click **Insert** from the upper navigation window ribbon menu and select **PivotTable**. Put the table layout inside a new worksheet block.
3. Move the **Sub-Category** column flag item inside the table template field list straight into the **Rows** layout quadrant.
4. Drag the **Sales** marker item entry down into the active **Values** matrix panel layout box.
5. Right-click the newly mapped values header block within the calculation matrix layout column field line, choice **Value Field Settings**, and update the aggregation summary behavior rule from *Sum* directly over to **Average**.
6. Sort the resulting column fields in descending order (*Largest to Smallest*) to confirm performance benchmarks. 
   * *Verification Check:* Top placements must report validation matches for **Copiers** (`2,198.94`) and **Machines** (`1,645.55`).

### Procedure 2: Extract Top 5 Profitable Customers
1. Create a clean, independent PivotTable instance targeting the core structural ledger rows.
2. Map **Customer Name** directly down onto the primary **Rows** display layout list column area.
3. Move the **Profit** category ledger data tag down directly across to populate inside the **Values** processing layout square (set calculation strictly to *Sum*).
4. Left-click the dropdown filtering toggle path selection point set adjacent right beside the **Row Labels** table label context block.
5. From the tracking options, choice **Value Filters** > select **Top 10...**.
6. Alter the numerical entry condition row filter settings boundary limit down from `10` to `5`, evaluating against your active **Sum of Profit** field matrix track.
7. Sort the field entries down in descending path layout rank.
   * *Verification Check:* Position slots must sequentially index matching profit validations for **Tamara Chand** (`8,981.32`), **Raymond Buch** (`6,976.09`), **Sanjit Chand** (`5,757.42`), **Hunter Lopez** (`5,622.43`), and **Adrian Barton** (`5,444.81`).

### Procedure 3: Build the Cross-Category Profit Temporal Matrix
1. Initialize a cross-tab style summary PivotTable using the operational row records asset group.
2. Place the transactional tracking variable data flag **Order Date** inside the tabular **Rows** processing field bucket. *(Note: Excel will auto-group this data by historical transaction Years)*.
3. Move the main structural **Category** tag option markers straight into the tracking tabular matrix **Columns** container sector layout fields.
4. Drop the target variable indicator column track marker **Profit** directly down inside your dynamic center data spreadsheet calculations box quadrant grid layout path (**Values** set to *Sum*).
   * *Verification Check:* Cross-referencing results check should match macro tracking matrix totals row year steps:
     * Year **2014** Total Profit: `49,544.06` [1]
     * Year **2015** Total Profit: `61,618.69` [1]
     * Year **2016** Total Profit: `81,795.27` [1]
     * Year **2017** Total Profit: `93,439.77` [1]
     * Cumulative Workbook Total Profit Sum baseline metrics target calculation: `286,397.79`.

---

