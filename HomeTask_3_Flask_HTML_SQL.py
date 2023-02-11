import json
from flask import Flask, request, render_template
import db_processing
from datetime import date

app = Flask(__name__)


@app.route("/user/", methods=['GET'])
def user_main():
    return "CRM's User"


@app.route("/user/email/", methods=['GET'])
def user_email():
    return "User's email"


@app.route("/user/email/credentials", methods=['GET'])
def user_email_creds():
    return "User's email credentials"


@app.route("/user/settings/", methods=['GET', 'PUT'])
def user_settings():
    return "User's settings"


@app.route("/user/documents/", methods=['GET', 'DELETE', 'PUT', 'POST'])
def user_documents():
    return "User's documents"


@app.route("/user/calendar/", methods=['GET', 'POST'])
def user_calendar():
    return "User's calendar"


@app.route("/user/template/", methods=['GET', 'DELETE', 'PUT', 'POST'])
def user_template():
    return "User's templates of letters"


# _______________info about vacancy______________
@app.route("/vacancy/", methods=['GET', 'POST'])
def list_vacancies():
    if request.method == 'POST':
        company = request.form.get('company')
        contacts_id = request.form.get('contacts_id')
        description = request.form.get('description')
        position_name = request.form.get('position_name')
        comment = request.form.get('comment')
        vacancy_data = {"user_id": 1, "creation_date": date.today(),
                        "position_name": position_name,
                        "company": company,
                        "description": description,
                        "contacts_id": contacts_id,
                        "comment": comment}
        db_processing.insert_db("vacancy", vacancy_data)
    result = db_processing.select_query_db("SELECT * from vacancy")
    return render_template('new_vacancy.html', vacancies=result)


@app.route("/vacancy/<id_vac>/", methods=['GET', 'PUT'])
def vacancy_id(id_vac):
    if request.method == 'GET':
        res_vacancy = db_processing.select_query_db(f"SELECT * from vacancy where id = {id_vac}")
        return render_template('id_vacancy_search.html', res_vacancy=res_vacancy, id_vac=id_vac)
    else:
        pass


@app.route("/vacancy/<id_vac>/event/", methods=['GET', 'POST'])
def vacancy_event(id_vac):
    if request.method == 'POST':
        description = request.form.get('description')
        event_date = request.form.get('event_date')
        title = request.form.get('title')
        due_to_date = request.form.get('due_to_date')
        status = request.form.get('status')
        event_data = {"vacancy_id": id_vac,
                      "description": description,
                      "event_date": event_date,
                      "title": title,
                      "due_to_date": due_to_date,
                      "status": status}
        db_processing.insert_db("events", event_data)
    res_event = db_processing.select_query_db(f"SELECT * from events where vacancy_id = {id_vac}")
    return render_template('event.html', event=res_event, id_vac=id_vac)


@app.route("/vacancy/<id_vac>/event/<id_event>/", methods=['GET'])
def vacancy_event_id(id_vac, id_event):
    if request.method == 'GET':
        res_id_event = db_processing.select_query_db(f"SELECT * from events where vacancy_id = {id_vac} and event_id={id_event}")
        return render_template('id_event_search.html', res_id_event=res_id_event, id_vac=id_vac, id_event=id_event)


@app.route("/vacancy/<id>/contact", methods=['GET', 'POST', 'PUT'])
def vacancy_contact():
    return "Dict of contacts with id_vacancy"


@app.route("/vacancy/<id>/history", methods=['GET'])
def vacancy_id_history():
    return "History of vacancies"


if __name__ == "__main__":
    app.run()
