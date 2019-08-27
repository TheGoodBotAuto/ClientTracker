from Models.contacts import Contact
from app import db

def get_all_contacts():
  return Contact.query.all()

def get_contact(id):
  contact = Contact.query.filter(Contact.contact_id == id).first()
  return contact

def add_contact(data):
  new_contact=populate_fields(Contact(),data)
  save_changes(new_contact)
  return new_contact
  
def update_contact(id,data):
  contact = Contact.query.filter(Contact.contact_id == id).first()
  if contact:
    populate_fields(contact,data)
    save_changes(contact)
  return contact

def populate_fields(contact, data):
  contact.contact_name=data.get('contact_name',contact.contact_name)
  contact.contact_email=data.get('contact_email', contact.contact_email)
  contact.contact_phone=data.get('contact_phone',contact.contact_phone)
  contact.application_id=data.get('application_id',contact.application_id)
  contact.customer_id=data.get('customer_id',contact.customer_id)
  return contact

def delete_contact(id):
  contact = Contact.query.filter(Contact.contact_id == id).first()
  db.session.delete(contact)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()