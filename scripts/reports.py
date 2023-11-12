#!/usr/bin/env python3

import reportlab

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics.charts.piecharts import Pie

def generate(filename, title, additional_info, table_data, chart, sales_by_made):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1, 20)

  chart_title = Paragraph(chart, styles["h2"])
  report_pie = Pie()
  report_pie.x = 100
  report_pie.y = 20
  report_pie.width = 150
  report_pie_height = 150
  report_pie.sideLabels = True
  report_pie.data = []
  report_pie.labels = []
  for make, sales in sales_by_made.items():
    report_pie.data.append(sales)
    report_pie.labels.append(make) 

  report_chart = Drawing(400, 150)
  #report_chart.add(Rect(1, 1, 399, 199, fillColor = colors.white))
  report_chart.add(report_pie)

  report.build([
    report_title,
    empty_line,
    report_info,
    empty_line,
    report_table,
    empty_line,
    chart_title,
    report_chart
   ])