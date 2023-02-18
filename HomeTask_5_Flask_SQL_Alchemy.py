from flask import Flask, request, render_template
import database_alchemy as db_al
from models import Vacancy, Event

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
    db_al.init_db()
    if request.method == 'POST':
        company = request.form.get('company')
        contacts_id = request.form.get('contacts_id')
        description = request.form.get('description')
        position_name = request.form.get('position_name')
        comment = request.form.get('comment')
        current_vacancy = Vacancy(position_name, company, description, contacts_id, comment, 1, 1)
        db_al.db_session.add(current_vacancy)
        db_al.db_session.commit()
    result = db_al.db_session.query(Vacancy).all()
    return render_template('new_vacancy.html', vacancies=result)


@app.route("/vacancy/<id_vac>/", methods=['GET'])
def vacancy_id(id_vac):
    db_al.init_db()
    if request.method == 'GET':
        res_vacancy = db_al.db_session.query(Vacancy).filter_by(id=id_vac).all()
    return render_template('id_vacancy_search.html', res_vacancy=res_vacancy, id_vac=id_vac)


@app.route("/vacancy/<id_vac>/event/", methods=['GET', 'POST'])
def vacancy_event(id_vac):
    db_al.init_db()
    if request.method == 'POST':
        vacancy_id = id_vac
        description = request.form.get('description')
        event_date = request.form.get('event_date')
        title = request.form.get('title')
        due_to_date = request.form.get('due_to_date')
        status = request.form.get('status')
        current_event = Event(vacancy_id, description, event_date, title, due_to_date, status)
        db_al.db_session.add(current_event)
        db_al.db_session.commit()
    res_event = db_al.db_session.query(Event).filter_by(vacancy_id=id_vac).all()
    return render_template('event.html', event=res_event, id_vac=id_vac)


@app.route("/vacancy/<id_vac>/event/<id_event>/", methods=['GET'])
def vacancy_event_id(id_vac, id_event):
    db_al.init_db()
    if request.method == 'GET':
        res_id_event = db_al.db_session.query(Event).filter_by(vacancy_id=id_vac, event_id=id_event).all()
    return render_template('id_event_search.html', res_id_event=res_id_event, id_vac=id_vac, id_event=id_event)


@app.route("/vacancy/<id>/contact", methods=['GET', 'POST', 'PUT'])
def vacancy_contact():
    return "Dict of contacts with id_vacancy"


@app.route("/vacancy/<id>/history", methods=['GET'])
def vacancy_id_history():
    return "History of vacancies"


if __name__ == "__main__":
    app.run()

