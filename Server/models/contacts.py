from app import db

class Contact(db.Model):
  __tablename__='contacts'
  contact_id = db.Column('contact_id',db.Integer,primary_key=True)
  contact_name = db.Column('contact_name', db.String())
  contact_email = db.Column('contact_email', db.String())
  contact_phone = db.Column('contact_phone', db.String())
  application_id = db.Column('application_id', db.Integer, db.ForeignKey('applications.application_id'))
  customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customers.customer_id'))
  
