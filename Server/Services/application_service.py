from Models.applications import Application
from app import db

def get_all_applications():
  return Application.query.all()

def add_application(data):
  new_application=Application(
    application_name=data['application_name'],
    customer_id= data['customer_id'],
    application_type=data['application_type']
    )
  save_changes(new_application)
  return new_application
  
def update_application(data):
  save_changes(data)
  return data

def save_changes(data):
  db.session.add(data)
  db.session.commit()