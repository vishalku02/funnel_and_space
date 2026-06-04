"""Load the collected explorable data into pandas DataFrames.

    from load_data import load_events, load_sessions
    events = load_events()      # long format: one row per interaction (the clickstream)
    sessions = load_sessions()  # wide format: one row per visit

Run `python3 load_data.py` for a quick summary.
"""

import glob
import json
import os

import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
EVENTS_FILE = os.path.join(DATA_DIR, "events.jsonl")
SESSIONS_DIR = os.path.join(DATA_DIR, "sessions")


def load_events():
    if not os.path.exists(EVENTS_FILE):
        return pd.DataFrame()
    with open(EVENTS_FILE, encoding="utf-8") as stream:
        rows = [json.loads(line) for line in stream if line.strip()]
    return pd.DataFrame(rows)


def load_sessions():
    rows = []
    for path in sorted(glob.glob(os.path.join(SESSIONS_DIR, "*.json"))):
        with open(path, encoding="utf-8") as stream:
            rows.append(json.load(stream))
    if not rows:
        return pd.DataFrame()

    flattened = []
    for snapshot in rows:
        row = {
            "session_id": snapshot.get("session_id"),
            "started_iso": snapshot.get("started_iso"),
            "duration_ms": snapshot.get("duration_ms"),
            "first_answer": snapshot.get("first_answer"),
            "final_answer": snapshot.get("final_answer"),
            "total_events": snapshot.get("total_events"),
        }
        for option_id, record in (snapshot.get("checkboxes") or {}).items():
            row["checkbox_" + option_id] = record.get("checked")
            row["checkbox_" + option_id + "_first_ms"] = record.get("first_checked_at_ms")
        for product, camp in (snapshot.get("card_sort_placements") or {}).items():
            row["sort_" + product] = camp
        flattened.append(row)
    return pd.DataFrame(flattened)


if __name__ == "__main__":
    events = load_events()
    sessions = load_sessions()
    print(f"events.jsonl   -> {len(events)} interactions")
    print(f"sessions/      -> {len(sessions)} visits")
    if not events.empty:
        print("\nevent types:")
        print(events["type"].value_counts())
    if not sessions.empty:
        print("\nsession columns:")
        print(list(sessions.columns))
