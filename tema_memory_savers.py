import uuid
import csv
import json
import os

id1 = uuid.uuid4()
id2 = uuid.uuid4()
id3 = uuid.uuid4()
id4 = uuid.uuid4()
id5 = uuid.uuid4()
id6 = uuid.uuid4()
id7 = uuid.uuid4()
id8 = uuid.uuid4()

cars = [
    {
        'id': id1,
        'brand': 'BMW',
        'model': '525',
        'hp': 190,
        'price': 5500,
    },
    {
        'id': id2,
        'brand': 'Audi',
        'model': 'A4',
        'hp': 140,
        'price': 3500,
    },
    {
        'id': id3,
        'brand': 'Skoda',
        'model': 'Octavia',
        'hp': 115,
        'price': 1800,
    },
    {
        'id': id4,
        'brand': 'Opel',
        'model': 'Insignia',
        'hp': 120,
        'price': 800,
    },
    {
        'id': id5,
        'brand': 'BMW',
        'model': '325',
        'hp': 110,
        'price': 2500,
    },
    {
        'id': id6,
        'brand': 'Seat',
        'model': 'Ibiza',
        'hp': 95,
        'price': 950,
    },
    {
        'id': id7,
        'brand': 'Skoda',
        'model': 'Rapid',
        'hp': 90,
        'price': 650,
    },
    {
        'id': id8,
        'brand': 'Ford',
        'model': 'Focus',
        'hp': 105,
        'price': 900,
    },
]

with open('file_exemples/input.csv', 'w') as my_file:
    writer = csv.writer(my_file)
    keys = cars[0].keys()
    writer.writerow(keys)
    for car in cars:
        writer.writerow(car.values())

dir = os.path.join("C:\\", "Python", "Memory savers", "output_data")
if not os.path.exists(dir):
    os.mkdir(dir)


sorted_slow_cars = list(filter(lambda slow: slow['hp'] < 120, cars))

with open('output_data/slow_cars.json', 'w') as json_file:
    json.dump(cars, json_file, indent=4)

sorted_fast_cars = list(filter(lambda fast: fast['hp'] >= 120 < 180, cars))

with open('output_data/fast_cars.json', 'w') as json_file:
    json.dump(sorted_fast_cars, json_file, indent=4)

sorted_sport_cars = list(filter(lambda sport: sport['hp'] >= 180, cars))

with open('output_data/sport_cars.json', 'w') as json_file:
    json.dump(sorted_sport_cars, json_file, indent=4)

sorted_cheap_cars = list(filter(lambda cheap: cheap['price'] < 1000, cars))

with open('output_data/cheap_cars.json', 'w') as json_file:
    json.dump(sorted_cheap_cars, json_file, indent=4)

sorted_medium_cars = list(filter(lambda medium: medium['price'] >= 1000 < 5000, cars))

with open('output_data/medium_cars.json', 'w') as json_file:
    json.dump(sorted_medium_cars, json_file, indent=4)

sorted_expensive_cars = list(filter(lambda expensive: expensive['price'] >= 5000, cars))

with open('output_data/expensive_cars.json', 'w') as json_file:
    json.dump(sorted_expensive_cars, json_file, indent=4)

