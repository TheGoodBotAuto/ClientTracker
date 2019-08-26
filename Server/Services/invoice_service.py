from Models.invoices import Invoice
from app import db

def get_all_invoices():
  return Invoice.query.all()

def get_invoice(id):
  invoice = Invoice.query.filter(Invoice.invoice_id == id).one()
  return invoice

def add_invoice(data):
  new_invoice=Invoice(
    invoice_number=data.get('invoice_number'),
    customer_id = data.get('customer_id'),
    hourly_rate = data.get('hourly_rate'),
    amount_billed = data.get('amount_billed'),
    description_of_service = data.get('description_of_service'),
    invoice_paid_date = data.get('invoice_paid_date')    
    )
  save_changes(new_invoice)
  return new_invoice
  
def update_invoice(data):
  save_changes(data)
  return data

def delete_invoice(id):
  invoice = Invoice.query.filter(Invoice.invoice_id == id).one()
  db.session.delete(invoice)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()