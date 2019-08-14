from app import db

class Customers(db.Model):
  __tablename__='customers'
  customer_id = db.Column(db.Integer,primary_key=True)
  customer_name = db.Column('customer_name', db.String())
  
