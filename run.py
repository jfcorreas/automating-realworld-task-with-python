#! /usr/bin/env python3
from pathlib import Path
import requests

source_path = Path.cwd() / 'data'
#web_service_url = 'http://34.83.170.114/feedback/'

for f in Path(source_path).iterdir():
  with open(f) as feedback_file:
    feedback_lines = feedback_file.readlines()
    feedback_entry = {
      'title': feedback_lines[0].rstrip(),
      'name': feedback_lines[1].rstrip(),
      'date': feedback_lines[2].rstrip(),
      'feedback': feedback_lines[3].rstrip()
    }
#    res = requests.post(web_service_url, feedback_entry)
#    res.raise_for_status()
#    print(res.status_code)
    