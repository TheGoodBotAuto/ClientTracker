from Models.applications import Application
from app import db

def get_all_applications():
  return Application.query.all()

def get_application(id):
  app = Application.query.filter(Application.application_id == id).first()
  return app

def add_application(data):
  new_application=populate_fields(Application(),data)
  save_changes(new_application)
  return new_application


def delete_application(id):
  app = Application.query.filter(Application.application_id == id).first()
  if not app:
    return None
  db.session.delete(app)
  db.session.commit()

def update_application(id,data):
  application = Application.query.filter(Application.application_id == id).first()
  if application:
    populate_fields(application,data)
    save_changes(application)
  return application

def populate_fields(application, data):
  application.application_name=data.get('application_name',application.application_name)
  application.application_type=data.get('application_type',application.application_type)
  application.customer_id=data.get('customer_id',application.customer_id)
  return application

def save_changes(data):
  db.session.add(data)
  db.session.commit()