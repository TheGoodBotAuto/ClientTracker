from Models.invoices import Invoice
from app import db

def get_all_invoices():
  return Invoice.query.all()

def get_invoice(id):
  invoice = Invoice.query.filter(Invoice.invoice_id == id).first()
  return invoice

def add_invoice(data):
  new_invoice=populate_fields(Invoice(),data)
  save_changes(new_invoice)
  return new_invoice
  
def update_invoice(id,data):
  invoice = Invoice.query.filter(Invoice.invoice_id == id).first()
  if invoice:
    populate_fields(invoice,data)
    save_changes(invoice)
  return invoice

def populate_fields(invoice, data):
  invoice.invoice_number=data.get('invoice_number',invoice.invoice_number)
  invoice.customer_id=data.get('customer_id',invoice.customer_id)
  invoice.hourly_rate=data.get('hourly_rate',invoice.hourly_rate)
  invoice.amount_billed=data.get('amount_billed',invoice.amount_billed)
  invoice.description_of_service=data.get('description_of_service',invoice.description_of_service)
  invoice.invoice_paid_date=data.get('invoice_paid_date',invoice.invoice_paid_date)

  return invoice

def delete_invoice(id):
  invoice = Invoice.query.filter(Invoice.invoice_id == id).first()
  db.session.delete(invoice)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()