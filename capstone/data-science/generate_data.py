import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(4031)

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
OUTPUT = BASE / "output"

DATA.mkdir(exist_ok=True)
OUTPUT.mkdir(exist_ok=True)

categories = [
    "Login Issues",
    "Network Issues",
    "Software Issues",
    "Hardware Issues",
    "Account Access",
]

start_date = datetime(2026, 7, 1)
records = []

for ticket_id in range(1, 10001):
    day = random.randint(0, 89)

    # Make sure the dataset covers exactly 90 days.
    if ticket_id == 1:
        day = 0
    elif ticket_id == 2:
        day = 89

    created_at = start_date + timedelta(
        days=day,
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
    )

    category = random.choices(
        categories,
        weights=[30, 20, 25, 15, 10],
        k=1,
    )[0]

    status = random.choices(
        ["Closed", "Open"],
        weights=[90, 10],
        k=1,
    )[0]

    resolution_hours = (
        round(random.uniform(1, 72), 2)
        if status == "Closed"
        else ""
    )

    records.append({
        "ticket_id": ticket_id,
        "created_at": created_at.isoformat(),
        "category": category,
        "status": status,
        "resolution_hours": resolution_hours,
    })

records.sort(key=lambda row: row["created_at"])

data_file = DATA / "incidents.csv"

with data_file.open("w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "ticket_id",
            "created_at",
            "category",
            "status",
            "resolution_hours",
        ],
    )
    writer.writeheader()
    writer.writerows(records)

dates = [
    datetime.fromisoformat(row["created_at"])
    for row in records
]

total_records = len(records)
days_covered = (
    max(dates).date() - min(dates).date()
).days + 1

missing_categories = sum(
    not row["category"] for row in records
)

missing_resolution = sum(
    row["status"] == "Closed"
    and row["resolution_hours"] == ""
    for row in records
)

duplicate_ids = total_records - len({
    row["ticket_id"] for row in records
})

checks = [
    ("total_records", total_records, ">=10000",
     total_records >= 10000),
    ("days_covered", days_covered, ">=90",
     days_covered >= 90),
    ("missing_categories", missing_categories, "0",
     missing_categories == 0),
    ("closed_missing_resolution", missing_resolution, "0",
     missing_resolution == 0),
    ("duplicate_ticket_ids", duplicate_ids, "0",
     duplicate_ids == 0),
]

quality_file = OUTPUT / "data_quality.csv"

with quality_file.open("w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["check", "value", "expected", "status"])
    for name, value, expected, passed in checks:
        writer.writerow([
            name,
            value,
            expected,
            "PASS" if passed else "FAIL",
        ])

print(f"Generated {total_records} incidents")
print(f"Days covered: {days_covered}")
print(f"Dataset: {data_file}")
print(f"Quality report: {quality_file}")

for name, value, expected, passed in checks:
    print(f"{name}: {value} -> {'PASS' if passed else 'FAIL'}")

if not all(passed for _, _, _, passed in checks):
    raise SystemExit("Data quality checks failed")
