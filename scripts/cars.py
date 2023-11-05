import json
import reports

most_sales_by_model = {}
most_sales_by_year = {}
cars_report = [
  ['ID', 'Car', 'Price', 'Total Sales']
]

with open("data/car_sales.json", "r") as file:
  car_sales = json.load(file)

  for car_data in car_sales:
    car = car_data['car']
    car_model = car['car_model']
    car_year = car['car_year']
    car_total_sales = car_data['total_sales']
    if car_model in most_sales_by_model:
      most_sales_by_model[car_model] =+ car_total_sales
    else:
      most_sales_by_model[car_model] = car_total_sales
    if car_year in most_sales_by_year:
      most_sales_by_year[car_year] =+ car_total_sales
    else:
      most_sales_by_year[car_year] = car_total_sales
    cars_report.append([
      car_data['id'],
      '{} {} ({})'.format(car['car_make'], car['car_model'], car['car_year']),
      car_data['price'],
      car_data['total_sales']
    ])

most_sales_by_model_sorted = dict(sorted(most_sales_by_model.items(), key=lambda item: item[1], reverse=True))
most_sales_by_year_sorted = dict(sorted(most_sales_by_year.items(), key=lambda item: item[1], reverse=True))

most_sales_model = list(most_sales_by_model_sorted.keys())[0]
best_model_summary = 'The {} had the most sales: {}'.format(most_sales_model, most_sales_by_model[most_sales_model])

most_sales_year = list(most_sales_by_year_sorted.keys())[0]
best_year_summary = 'The most popular year was {} with {} sales.'.format(most_sales_year, most_sales_by_year[most_sales_year])

reports.generate(
  "output/cars.pdf",
  "Sales summary for last month",
  '{}<br/>{}<br/>'.format(best_model_summary, best_year_summary),
   cars_report
)