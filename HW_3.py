from flask import Flask, request
from faker import Faker
import csv
from statistics import mean
import requests


app = Flask(__name__)


@app.route("/requirements/")
def requirements():
    with open(r'C:\Users\Котик\PycharmProjects\PythoProFlask\requirements.txt', "r") as file:
        requirement = file.read()
    return '<pre>{}</pre>'.format(requirement)


@app.route("/generate-users/")
def generate_users():
    fake = Faker()
    list_name_mail = []
    users_count = request.args.get('count', 0, type=int)
    for i in range(users_count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}_{last_name.lower()}@example.com"
        list_name_mail.append(f"{first_name} {last_name}, {email}")
    res = '\n'.join(list_name_mail)
    return '<pre>{}</pre>'.format(res)


@app.route("/mean/")
def avarage():
    with open(r'C:\Users\Котик\PycharmProjects\PythoProFlask\hw.csv', "r") as file:
        reader = csv.DictReader(file)
        height = []
        weight = []
        for i in reader:
            height_cm = float(i[' "Height(Inches)"'])*2.54
            weight_kg = float(i[' "Weight(Pounds)"'])/2.205
            height.append(height_cm)
            weight.append(weight_kg)
        average_h = mean(height)
        average_w = mean(weight)
        res = f'average height is : {round(average_h,2)} cm, Average weight is: {round(average_w,2)} kg'
    return res


@app.route("/space/")
def astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    space_station = r.json()
    numb_astronauts = space_station['number']
    return f' Number of astronauts right now in the space: {numb_astronauts}'