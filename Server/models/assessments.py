from app import db

class Assessments(db.Model):
  __tablename__='assessments'
  assessment_id = db.Column(db.Integer,primary_key=True)
  start_date = db.Column('start_date', db.Date)
  completed_date = db.Column('completed_date', db.Date)
  total_hours = db.Column('total_hours', db.Numeric)
  invoice_id = db.Column('invoice_id', db.Integer, db.ForeignKey('invoices.id'))
  
