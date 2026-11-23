# Applied Data Science - Data Plan

## Business Problem

Our incident tracking system needs a way to understand how many
support tickets are created, which categories are most common,
and how long tickets take to resolve.

The goal is to use this information to recommend how many
support agents are needed. The team currently has 6 agents.

## Data Decision

I chose Approach B: generate synthetic incident data using Python.

The current PostgreSQL database contains only 4 tickets, which
is not enough for meaningful analysis. Instead of changing the
existing database, I will create a separate CSV dataset.

This dataset will be used for the capstone analysis. The existing
Flask application and PostgreSQL database will remain unchanged.

## Dataset Requirements

- At least 10,000 incident records
- At least 90 days of data
- Every incident has a category
- Every closed incident has a resolution time
- No real customer information
- Reproducible generation using a fixed random seed

## Planned Fields

- ticket_id: Unique incident identifier
- created_at: Date and time the ticket was created
- category: Type of incident
- status: Open or Closed
- resolution_hours: Hours needed to resolve a closed ticket

## Planned Categories

- Login Issues
- Network Issues
- Software Issues
- Hardware Issues
- Account Access

## Data Quality Checks

The data quality report will verify:

1. Total number of records
2. Number of days covered
3. Missing categories
4. Closed incidents missing resolution times
5. Duplicate ticket IDs

## Reproducibility

The Python generator will use a fixed random seed so the
same dataset can be recreated.

The generated dataset will be saved in:
capstone/data-science/data/incidents.csv

The quality report will be saved in:
capstone/data-science/output/data_quality.csv

## Limitations

The dataset is synthetic, so it does not represent actual
customer activity. Any staffing recommendation will be based
on simulated incident patterns and stated assumptions.
