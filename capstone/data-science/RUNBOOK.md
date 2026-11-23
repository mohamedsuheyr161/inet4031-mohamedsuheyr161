# Applied Data Science - Runbook

## Project Overview

This project uses synthetic incident data to analyze support
ticket volume, incident categories, and resolution times.

The goal is to recommend staffing levels for a support team
that currently has 6 agents.

## Environment

- Ubuntu VM
- Python 3.14.4
- Python virtual environment
- pandas, matplotlib, scipy, csvkit
- GitHub repository: inet4031-mohamedsuheyr161
- Branch: capstone-data-science

## Environment Checkpoint

The Week 11 checkpoint verified:
- Kubernetes node was Ready
- Application and database pods were Running
- Flask health endpoint returned OK
- Prometheus targets were healthy

Evidence:
environment-checkpoint.txt

## Python Setup

Install the virtual environment package:

sudo apt update
sudo apt install -y python3.14-venv

Create the virtual environment:

python3 -m venv ~/data-science-venv

Install the required Python packages:

~/data-science-venv/bin/pip install -r capstone/data-science/requirements.txt

## Generate the Dataset

From the repository root, run:

~/data-science-venv/bin/python capstone/data-science/generate_data.py

This creates:
- data/incidents.csv
- output/data_quality.csv

## Verify the Dataset

Run:

cat capstone/data-science/output/data_quality.csv

wc -l capstone/data-science/data/incidents.csv

Expected results:
- 10,000 incidents
- 90 days covered
- 0 missing categories
- 0 closed tickets missing resolution times
- 0 duplicate ticket IDs
- All quality checks PASS

## Week 11 Baseline

The existing PostgreSQL database contained 4 tickets.

The synthetic dataset contains 10,000 tickets across 90 days.

The synthetic dataset is stored separately and does not
modify the existing PostgreSQL database.

## Future Work

Week 12:
- Generate three analysis CSV files
- Generate three PNG charts
- Perform one statistical check
- Create one command to regenerate the analysis

Week 13:
- Write the staffing recommendation report
- Complete the documentation
- Rebuild and verify the project on a clean VM
