from app import db

class Applications(db.Model):
  __tablename__='applications'
  application_id = db.Column(db.Integer,primary_key=True)
  application_name = db.Column('application_name', db.String())
  customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'))
  application_type = db.Column('application_type', db.String())
