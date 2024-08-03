import json
import csv

# Your JSON data
data = [
    {
        "tables": ["covid_testing_states_daily", "covid_testing_us_daily"],
        "sql": "SELECT * FROM covid_testing_states_daily ctsd JOIN covid_testing_us_daily ctud ON ctsd.date = ctud.date"
    },
    {
        "tables": ["covid_testing_states_daily", "nytimes_counties"],
        "sql": "SELECT * FROM covid_testing_states_daily ctsd JOIN nytimes_counties nc ON ctsd.date = nc.date"
    }
]

# Convert JSON to CSV
csv_file = "data.csv"
csv_columns = ["tables", "sql"]

with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for entry in data:
        entry['tables'] = ','.join(entry['tables'])  # Convert list to comma-separated string
        writer.writerow(entry)