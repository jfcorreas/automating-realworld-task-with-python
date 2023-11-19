#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime
import reports

source_path = Path.cwd() / 'supplier-data' / 'descriptions'
report_path = '/tmp/processed.pdf'

def main():
  report_title = 'Processed Update on {}'.format(
    datetime.now().strftime('%d-%b-%Y')
  )
  report_paragraph = []
  for description_file in Path(source_path).iterdir():
    with open(description_file) as opened:
      description_line = opened.readlines()
      report_paragraph.append('name: {}'.format(description_line[0].rstrip()))
      report_paragraph.append('weight: {}'.format(description_line[1].rstrip()))
  reports.generate_report(report_path, report_title, '<br/>'.join(report_paragraph))

if __name__ == "__main__":
    main()