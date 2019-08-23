from Models.contacts import Contact
from app import db

def get_all_contacts():
  return Contact.query.all()

def add_contact(data):
  new_contact=Contact(
    contact_name=data['contact_name'],
    contact_email=data['contact_email'],
    contact_phone=data['contact_phone'],
    application_id=data['application_id'],
    customer_id=data['customer_id']
    )
  save_changes(new_contact)
  return new_contact
  
def update_contact(data):
  save_changes(data)
  return data

def save_changes(data):
  db.session.add(data)
  db.session.commit()