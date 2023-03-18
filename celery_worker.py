from celery import Celery
import database_alchemy
from email_con import EmailWrapper
from models import EmailCredentials
import os

RABBIT_HOST = os.environ.get('RABBITHOST', 'localhost')

app = Celery('celery_worker', broker=f'pyamqp://guest:guest@{RABBIT_HOST}:5672//')


@app.task()
def send_email(id_email_creds, recipient, message):
    database_alchemy.init_db()
    email_creds_detail = database_alchemy.db_session.query(EmailCredentials).get(id_email_creds)
    email_wrapper = EmailWrapper(**email_creds_detail.get_mandatory_fields())
    email_wrapper.send_email(recipient, message)

