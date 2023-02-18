from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from datetime import date
from database_alchemy import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    login = Column(String(50), unique=True)
    password = Column(String(50))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name


class EmailCredentials(Base):
    __tablename__ = 'emailcredentials'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    email = Column(String(120), unique=True, nullable=False)
    login = Column(String(120), nullable=False)
    password = Column(String(50), nullable=False)
    pop_server = Column(String(120), nullable=False)
    smtp_server = Column(String(120), nullable=False)

    def __init__(self, login, password):
        self.login = login
        self.password = password


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    position_name = Column(String(120), nullable=False)
    company = Column(String(120), nullable=False)
    description = Column(String(500), nullable=False)
    contacts_id = Column(String(120), nullable=False)
    creation_date = Column(DateTime, default=date.today())
    comment = Column(String(250), nullable=True)
    status = Column(Integer, nullable=False)

    def __init__(self, position_name, company, description, contacts_id, comment, status, user_id):
        self.position_name = position_name
        self.company = company
        self.description = description
        self.contacts_id = contacts_id
        self.comment = comment
        self.status = status
        self.user_id = user_id

    def __repr__(self):
        return '<Vacancy %r>' % self.position_name


class Event(Base):
    __tablename__ = 'events'
    event_id = Column(Integer, primary_key=True, autoincrement=True)
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    description = Column(String(500), nullable=False)
    event_date = Column(String, default=date.today())
    title = Column(String(120), nullable=True)
    due_to_date = Column(String, default=date.today())
    status = Column(Integer, nullable=False)

    def __init__(self, vacancy_id, description, event_date, title, due_to_date, status):
        self.vacancy_id = vacancy_id
        self.description = description
        self.event_date = event_date
        self.title = title
        self.due_to_date = due_to_date
        self.status = status

    def __repr__(self):
        return '<Event %r>' % self.title


class Template(Base):
    __tablename__ = 'template'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __repr__(self):
        return '<Template %r>' % self.name


class Document(Base):
    __tablename__ = 'document'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    content = Column(Text, nullable=False)
    description = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, name, content, description):
        self.name = name
        self.content = content
        self.description = description

    def __repr__(self):
        return '<Document %r>' % self.name
