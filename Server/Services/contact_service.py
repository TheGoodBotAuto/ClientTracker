from Models.contacts import Contact
from app import db

def get_all_contacts():
  return Contact.query.all()

def get_contact(id):
  contact = Contact.query.filter(Contact.contact_id == id).one()
  return contact

def add_contact(data):
  new_contact=Contact(
    contact_name=data.get('contact_name'),
    contact_email=data.get('contact_email'),
    contact_phone=data.get('contact_phone'),
    application_id=data.get('application_id'),
    customer_id=data.get('customer_id')
    )
  save_changes(new_contact)
  return new_contact
  
def update_contact(data):
  save_changes(data)
  return data

def delete_contact(id):
  contact = Contact.query.filter(Contact.contact_id == id).one()
  db.session.delete(contact)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()