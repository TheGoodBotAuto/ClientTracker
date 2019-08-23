from Models.invoices import Invoice
from app import db

def get_all_invoices():
  return Invoice.query.all()

def add_invoice(data):
  new_invoice=Invoice(
    invoice_number=data['invoice_number'],
    customer_id = data['customer_id'],
    hourly_rate = data['hourly_rate'],
    amount_billed = data['amount_billed'],
    description_of_service = data ['description_of_service'],
    invoice_paid_date = data['invoice_paid_data']    
    )
  save_changes(new_invoice)
  return new_invoice
  
def update_invoice(data):
  save_changes(data)
  return data

def save_changes(data):
  db.session.add(data)
  db.session.commit()