# QA Report - Applied Data Science Capstone

## Test Information

Environment: Local Ubuntu VM
Track: Applied Data Science
Tester: Mohamed Osman
Status: Test cases drafted before implementation

## Test Case 1: Dataset Size and Date Range

Criterion: Dataset contains 10,000+ incidents over 90+ days.
Type: Positive

Preconditions: Dataset generator has been implemented.
Steps:
1. Run the Python dataset generator.
2. Open data/incidents.csv.
3. Count the records and check the earliest and latest dates.

Expected Result:
At least 10,000 records covering at least 90 days.

Actual Result: Pending
Status: Not Run

## Test Case 2: Required Data Fields

Criterion: Every incident has a category, and every closed incident
has a resolution time.
Type: Positive

Preconditions: Dataset exists.
Steps:
1. Load incidents.csv.
2. Check for missing categories.
3. Check closed tickets for missing resolution times.
4. Check for duplicate ticket IDs.

Expected Result:
Zero missing categories, zero closed tickets missing resolution
times, and zero duplicate ticket IDs.

Actual Result: Pending
Status: Not Run

## Test Case 3: Analysis Outputs

Criterion: Three analysis CSV files.
Type: Positive

Preconditions: Analysis pipeline has been implemented.
Steps:
1. Run the analysis command.
2. Check the output folder.

Expected Result:
Three CSV files showing weekly incident volume, resolution
times by category, and category rankings.

Actual Result: Pending
Status: Not Run

## Test Case 4: Charts

Criterion: Three labeled PNG charts.
Type: Positive

Preconditions: Analysis pipeline has been implemented.
Steps:
1. Run the analysis command.
2. Check the output folder.

Expected Result:
Three PNG charts with titles and labeled axes.

Actual Result: Pending
Status: Not Run

## Test Case 5: Statistical Check and Staffing Report

Criterion: Statistical evidence and staffing recommendation.
Type: Positive

Preconditions: Analysis has been completed.
Steps:
1. Review the statistical results.
2. Review report.md.

Expected Result:
At least one numerical statistical check with a plain-English
interpretation and a report recommending a specific number of agents.

Actual Result: Pending
Status: Not Run

## Test Case 6: Invalid Data

Criterion: Data validation.
Type: Negative

Preconditions: Data validation has been implemented.
Steps:
1. Provide a dataset with a missing category.
2. Run the validation process.

Expected Result:
The validation detects the missing category and reports a failure.

Actual Result: Pending
Status: Not Run

## Rebuild Verification - Week 13

Run the pipeline on a rebuilt VM and confirm that the dataset,
analysis CSVs, charts, and statistical results can be regenerated.

Expected Result:
The rebuilt VM produces the required outputs successfully.

Actual Result: Pending
Status: Not Run

## Final Sign-Off

Overall Status: Pending
Date: Pending
