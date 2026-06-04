"""Serves the explorable and records anonymous clickstream data.

Run:  python3 server.py
Then open the printed http://localhost:8000 URL.

Two things get written under data/:
  data/events.jsonl              one JSON object per interaction (the raw clickstream)
  data/sessions/<id>.json        one wide snapshot per visit (first answer, every
                                 checkbox, the card sort, the final answer, timings)
No names or identifiers are collected; each visit gets a random session id.
"""

import http.server
import json
import os
import re
import socketserver
import threading
from datetime import datetime, timezone

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
EVENTS_FILE = os.path.join(DATA_DIR, "events.jsonl")
SESSIONS_DIR = os.path.join(DATA_DIR, "sessions")
write_lock = threading.Lock()
safe_session_id = re.compile(r"[^A-Za-z0-9_-]")


def server_received_at():
    return datetime.now(timezone.utc).isoformat()


class ExplorableHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def read_json_body(self):
        length = int(self.headers.get("Content-Length", 0))
        if length == 0:
            return None
        raw = self.rfile.read(length)
        return json.loads(raw.decode("utf-8"))

    def reply_no_content(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if self.path == "/log":
            self.handle_event_log()
        elif self.path == "/snapshot":
            self.handle_snapshot()
        else:
            self.send_error(404)

    def handle_event_log(self):
        event = self.read_json_body() or {}
        event["server_received_at"] = server_received_at()
        with write_lock:
            with open(EVENTS_FILE, "a", encoding="utf-8") as stream:
                stream.write(json.dumps(event) + "\n")
        self.reply_no_content()

    def handle_snapshot(self):
        snapshot = self.read_json_body() or {}
        snapshot["server_received_at"] = server_received_at()
        raw_id = str(snapshot.get("session_id", "unknown"))
        session_id = safe_session_id.sub("_", raw_id) or "unknown"
        destination = os.path.join(SESSIONS_DIR, session_id + ".json")
        with write_lock:
            with open(destination, "w", encoding="utf-8") as stream:
                json.dump(snapshot, stream, indent=2)
        self.reply_no_content()

    def log_message(self, format, *args):
        pass


def main():
    os.makedirs(SESSIONS_DIR, exist_ok=True)
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", PORT), ExplorableHandler) as httpd:
        print(f"Serving the explorable at http://localhost:{PORT}")
        print(f"Recording clickstream to {EVENTS_FILE}")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
