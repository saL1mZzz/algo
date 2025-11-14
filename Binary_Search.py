# STEP 6 — BINARY SEARCH BY DATE (simple)
# =======================================
# Assumes:
# - The dataset (list of rows) is already sorted by date ascending.
# - Each row is a dictionary or list where the date is accessible as row["Date"] or row[0].
# - The target date is provided in 'YYYY-MM-DD' format.
#
# Goal:
# - Find all entries that match the target date using binary search on the Date column.

import csv
from datetime import datetime

with open(file="daily_orders_detailed.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)
    data = list(reader)

def parse_date(date_str):
# Convert a 'YYYY-MM-DD' string to a date object.
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def binary_search_by_date(data, target_date_str):

# Perform binary search on a sorted list of rows by their 'Date' column.
# Returns a list of all rows that match the given date.

    if not data:
        return "The dataset is empty."
    if not isinstance(data, list):
        return "No list was provided."

    target_date = parse_date(target_date_str)

    start = 0
    end = len(data) - 1
    found_index = None

    while start <= end:
        mid = (start + end) // 2
        mid_date = parse_date(data[mid]["Date"])

        if mid_date == target_date:
            found_index = mid
            break
        elif mid_date < target_date:
            start = mid + 1
        else:
            end = mid - 1

    if found_index is None: # If not found, return None
        return None

    results = [data[found_index]] # Expand to include all rows with the same date

    # Check previous rows
    i = found_index - 1
    while i >= 0 and parse_date(data[i]["Date"]) == target_date:
        results.insert(0, data[i])
        i -= 1

    # Check next rows
    j = found_index + 1
    while j < len(data) and parse_date(data[j]["Date"]) == target_date:
        results.append(data[j])
        j += 1

    return results