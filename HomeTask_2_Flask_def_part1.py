import json
from flask import Flask

app = Flask(__name__)

file_vac = "vacancies_data.json"
vacancy_data = json.load(open(file_vac, mode='r', encoding='utf-8'))
file_events = "events_data.json"
events_data = json.load(open(file_events, mode='r', encoding='utf-8'))

#_______________info about user___________________
@app.route("/user/", methods = ['GET'])
def user_main():
    return "CRM's User"

@app.route("/user/email/", methods = ['GET'])
def user_email():
    return "User's email"

@app.route("/user/email/credentials", methods = ['GET'])
def user_email_creds():
    return "User's email credentials"

@app.route("/user/settings/", methods = ['GET', 'PUT'])
def user_settings():
    return "User's settings"

@app.route("/user/documents/", methods = ['GET', 'DELETE', 'PUT', 'POST'])
def user_documents():
    return "User's documents"

@app.route("/user/calendar/", methods = ['GET', 'POST'])
def user_calendar():
    return "User's calendar"

@app.route("/user/template/", methods = ['GET', 'DELETE', 'PUT', 'POST'])
def user_template():
    return "User's templates of letters"

#_______________info about vacancy______________
@app.route("/vacancy/", methods = ['GET', 'POST'])
def list_vacancies():
    return vacancy_data

@app.route("/vacancy/<id_vac>/", methods = ['GET', 'PUT'])
def vacancy_id(id_vac):
    for vacancy in vacancy_data:
        if vacancy['id'] == id_vac:
            return vacancy

@app.route("/vacancy/<id_vac>/event", methods = ['GET', 'POST'])
def vacancy_event(id_vac):
    event_list = []
    for event in events_data:
        if event['vacancy_id'] == id_vac:
            event_list.append(event)
    return event_list

@app.route("/vacancy/<id_vac>/event/<id_event>", methods = ['GET'])
def vacancy_event_id(id_vac, id_event):
    for event in events_data:
        if event['id'] == id_event:
            return event

@app.route("/vacancy/<id>/contact", methods = ['GET', 'POST', 'PUT'])
def vacancy_contact():
    return "Dict of contacts with id_vacancy"

@app.route("/vacancy/<id>/history", methods = ['GET'])
def vacancy_id_history():
    return "History of vacancies"
