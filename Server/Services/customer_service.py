from Models.customers import Customer
from app import db

def get_all_customers():
  return Customer.query.all()

def get_customer(id):
  customer = Customer.query.filter(Customer.customer_id == id).first()
  return customer

def add_customer(data):
  new_customer=populate_fields(Customer(),data)
  save_changes(new_customer)
  return new_customer
  
def update_customer(id,data):
  customer = Customer.query.filter(Customer.customer_id == id).first()
  if customer:
    populate_fields(customer,data)
    save_changes(customer)
  return customer

def delete_customer(id):
  customer = Customer.query.filter(Customer.customer_id == id).first()
  db.session.delete(customer)
  db.session.commit()

def populate_fields(customer, data):
  customer.customer_name=data.get('customer_name',customer.customer_name)
  return customer

def save_changes(data):
  db.session.add(data)
  db.session.commit()