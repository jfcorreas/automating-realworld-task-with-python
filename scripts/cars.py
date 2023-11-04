import json

most_sales_by_model = {}
most_sales_by_year = {}

with open("data/car_sales.json", "r") as file:
  car_sales = json.load(file)
  for car in car_sales:
    car_model = car['car']['car_model']
    car_year = car['car']['car_year']
    car_sales = car['total_sales']
    if car_model in most_sales_by_model:
      most_sales_by_model[car_model] =+ car_sales
    else:
      most_sales_by_model[car_model] = car_sales
    if car_year in most_sales_by_year:
      most_sales_by_year[car_year] =+ car_sales
    else:
      most_sales_by_year[car_year] = car_sales

print(dict(sorted(most_sales_by_model.items(), key=lambda item: item[1], reverse=True)))
print(dict(sorted(most_sales_by_year.items(), key=lambda item: item[1], reverse=True)))