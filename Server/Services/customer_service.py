from Models.customers import Customer
from app import db

def get_all_customers():
  return Customer.query.all()

def get_customer(id):
  customer = Customer.query.filter(Customer.customer_id == id).one()
  return customer

def add_customer(data):
  new_customer=Customer(customer_name=data.get('customer_name'))
  save_changes(new_customer)
  return new_customer
  
def update_customer(data):
  save_changes(data)
  return data

def delete_customer(id):
  customer = Customer.query.filter(Customer.customer_id == id).one()
  db.session.delete(customer)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()