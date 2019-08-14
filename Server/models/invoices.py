from app import db

class Invoices(db.Model):
  __tablename__='invoices'
  invoice_id = db.Column(db.Integer,primary_key=True)
  invoice_number = db.Column('invoice_number', db.Integer)
  customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'))
  hourly_rate = db.Column('hourly_rate', db.Numeric)
  amount_billed = db.Column('amount_billed', db.Numeric)
  description_of_service = db.Column('description_of_service', db.String())
  invoice_paid_date = db.Column('invoice_paid_date', db.Date)