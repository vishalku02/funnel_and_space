#!/usr/bin/env bash
set -euo pipefail

script_directory="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
server_url="http://localhost:8000"

python3 "$script_directory/server.py" &
server_process_id=$!
trap 'kill "$server_process_id" 2>/dev/null' EXIT

sleep 1
open "$server_url"

wait "$server_process_id"
