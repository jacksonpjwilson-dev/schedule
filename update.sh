#!/usr/bin/env bash
# Regenerate data/schedule.json and push. Usage: ./update.sh [path/to/schedule.json]
# With an argument, copies that JSON in (bumping "updated"); otherwise runs gen.py.
set -e; cd "$(dirname "$0")"
if [ -n "$1" ]; then python3 - "$1" <<'P'
import json,sys,datetime
d=json.load(open(sys.argv[1]));d["updated"]=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
json.dump(d,open("data/schedule.json","w"),indent=1,ensure_ascii=False)
P
else python3 gen.py; fi
git add -A && git commit -qm "Update schedule $(date -u +%FT%TZ)" && git push -q && echo pushed
