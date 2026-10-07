#!/usr/bin/env python3
"""Controlled detection-validation runner for training only."""
import csv, sys

path = sys.argv[1] if len(sys.argv) > 1 else "de-validation-practical.csv"

def draft_detection(row):
    # Draft v1 intentionally recognizes only the long -EncodedCommand form.
    return (
        row["process"].lower() == "powershell.exe"
        and row["parent_process"].lower() == "wscript.exe"
        and "-encodedcommand" in row["command_line"].lower()
    )

rows = list(csv.DictReader(open(path, newline="")))
print("event_id expected actual telemetry result")
false_negatives = []
false_positives = []
data_gaps = []
for row in rows:
    actual = draft_detection(row)
    expected_target = row["expected_class"].startswith("target")
    if row["telemetry_complete"].lower() != "true":
        data_gaps.append(row["event_id"])
    if expected_target and not actual and row["telemetry_complete"].lower() == "true":
        false_negatives.append(row["event_id"])
    if (not expected_target) and actual:
        false_positives.append(row["event_id"])
    print(row["event_id"], row["expected_class"], "MATCH" if actual else "NO_MATCH", row["telemetry_complete"])

print("\nSummary")
print("false_negatives:", ", ".join(false_negatives) or "none")
print("false_positives:", ", ".join(false_positives) or "none")
print("data_path_gaps:", ", ".join(data_gaps) or "none")
