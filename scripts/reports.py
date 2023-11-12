#!/usr/bin/env python3

import reportlab

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart

def generate(filename, title, additional_info, table_data, pie_title, sales_by_made, bar_title, sales_by_model ):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1, 20)

  chart_title = Paragraph(pie_title, styles["h2"])
  report_pie = Pie()
  report_pie.x = 120
  report_pie.y = 40
  report_pie.width = 125
  report_pie.sideLabels = True
  report_pie.data = []
  report_pie.labels = []
  for make, sales in sales_by_made.items():
    report_pie.data.append(sales)
    report_pie.labels.append(make) 

  chart2_title = Paragraph(bar_title, styles["h2"])
  report_bar = VerticalBarChart()
  report_bar.x = 50
  report_bar.y = 20
  report_bar.width = 300
  report_bar.height = 150
  data = []
  report_bar.categoryAxis.categoryNames = []
  for car_model, sales in sales_by_model.items():
    data.append(int(sales['revenue']/1000000))
    report_bar.categoryAxis.categoryNames.append(car_model)
  report_bar.data = [tuple(data)]

  report_bar.valueAxis.valueMin = 0
  report_bar.valueAxis.valueMax = 30
  report_bar.valueAxis.valueStep = 5
  report_bar.categoryAxis.labels.boxAnchor = 'ne'
  report_bar.categoryAxis.labels.dx = 8
  report_bar.categoryAxis.labels.dy = -2
  report_bar.categoryAxis.labels.angle = 30
     
  report_chart = Drawing(400, 200)
  report_chart2 = Drawing(400, 200)
  report_chart.add(report_pie)
  report_chart2.add(report_bar)

  report.build([
    report_title,
    empty_line,
    report_info,
    empty_line,
    report_table,
    empty_line,
    chart_title,
    report_chart,
    chart2_title,
    report_chart2
   ])