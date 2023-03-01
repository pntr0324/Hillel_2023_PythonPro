from flask import Flask, request, render_template
import database_alchemy as db_al
from models import Vacancy, Event, EmailCredentials
import email_con

app = Flask(__name__)


@app.route("/user/", methods=['GET'])
def user_main():
    return "CRM's User"


@app.route("/user/email/", methods=['GET', 'POST'])
def user_email():
    user_settings = db_al.db_session.query(EmailCredentials).filter_by(user_id=1).first()
    email_obj = email_con.EmailWrapper(
        user_settings.login,
        user_settings.password,
        user_settings.email,
        user_settings.smtp_server,
        user_settings.smtp_port,
        user_settings.pop_server,
        user_settings.pop_port,
        user_settings.imap_server,
        user_settings.imap_port
    )
    if request.method == 'POST':
        recipient = request.form.get('recipient')
        email_message = request.form.get('email_message')
        email_obj.send_email(recipient, email_message)
        return 'Send email'
    emails = email_obj.get_emails([1], protocol='pop3')
    return render_template('send_email.html', emails=emails)


@app.route("/user/email/credentials", methods=['GET'])
def user_email_creds():
    return "User's email credentials"


@app.route("/user/settings/", methods=['GET', 'PUT'])
def user_settings_1():
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


@app.route("/vacancy/<id_vac>/", methods=['GET', 'POST'])
def vacancy_id(id_vac):
    db_al.init_db()
    if request.method == 'POST':
        position_name = request.form.get('position_name')
        company = request.form.get('company')
        description = request.form.get('description')
        contacts_id = request.form.get('contacts_id')
        comment = request.form.get('comment')
        status = request.form.get('status')
        edited_vac = {
            Vacancy.position_name: position_name,
            Vacancy.company: company,
            Vacancy.description: description,
            Vacancy.contacts_id: contacts_id,
            Vacancy.comment: comment,
            Vacancy.status: status
        }
        db_al.db_session.query(Vacancy).filter(Vacancy.id == id_vac).\
            update(edited_vac, synchronize_session=False)
        db_al.db_session.commit()
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


@app.route("/vacancy/<id_vac>/event/<id_event>/", methods=['GET', 'POST'])
def vacancy_event_id(id_vac, id_event):
    db_al.init_db()
    if request.method == 'POST':
        description = request.form.get('description')
        event_date = request.form.get('event_date')
        title = request.form.get('title')
        due_to_date = request.form.get('due_to_date')
        status = request.form.get('status')
        edited_event = {
            Event.description: description,
            Event.event_date: event_date,
            Event.title: title,
            Event.due_to_date: due_to_date,
            Event.status: status
        }
        db_al.db_session.query(Event).filter(Event.event_id == id_event, Event.vacancy_id == id_vac).\
            update(edited_event, synchronize_session=False)
        db_al.db_session.commit()
    res_id_event = db_al.db_session.query(Event).filter_by(vacancy_id=id_vac, event_id=id_event).all()
    return render_template('id_event_search.html', res_id_event=res_id_event, id_vac=id_vac, id_event=id_event)


@app.route("/vacancy/<id>/contact", methods=['GET', 'POST', 'PUT'])
def vacancy_contact():
    return "Dict of contacts with id_vacancy"


@app.route("/vacancy/<id>/history", methods=['GET'])
def vacancy_id_history():
    return "History of vacancies"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

