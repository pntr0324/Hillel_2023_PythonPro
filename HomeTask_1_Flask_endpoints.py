from flask import Flask

app = Flask(__name__)

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
    return "List of vacancies"

@app.route("/vacancy/<id/>", methods = ['GET', 'PUT'])
def vacancy_id():
    return "Show vacancy's content with id"

@app.route("/vacancy/<id>/contact", methods = ['GET', 'POST', 'PUT'])
def vacancy_contact():
    return "Dict of contacts with id_vacancy"

@app.route("/vacancy/<id>/event", methods = ['GET', 'POST'])
def vacancy_event():
    return "List of events"

@app.route("/vacancy/<id>/event/<id_event>", methods = ['GET'])
def vacancy_event_id():
    return "Show event's content with id"

@app.route("/vacancy/<id>/history", methods = ['GET'])
def vacancy_id_history():
    return "History of vacancies"
