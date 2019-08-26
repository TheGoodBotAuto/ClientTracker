from Models.applications import Application
from app import db

def get_all_applications():
  return Application.query.all()

def get_application(id):
  app = Application.query.filter(Application.application_id == id).one()
  return app

def add_application(data):
  new_application=Application(
    application_name=data.get('application_name'),
    customer_id= data.get('customer_id'),
    application_type=data.get('application_type')
    )
  save_changes(new_application)
  return new_application
  
def update_application(data):
  save_changes(data)
  return data

def delete_application(id):
  app = Application.query.filter(Application.application_id == id).one()
  db.session.delete(app)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()