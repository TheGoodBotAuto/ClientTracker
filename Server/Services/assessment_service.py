from Models.assessments import Assessment
from app import db

def get_all_assessments():
  return Assessment.query.all()

def add_assessment(data):
  new_assessment=Assessment(
    start_date=data['start_date'],
    completed_date = data['completed_date'],
    total_hours = data['total_hours'],
    invoice_id = data['invoice_id']
    )
  save_changes(new_assessment)
  return new_assessment
  
def update_assessment(data):
  save_changes(data)
  return data

def save_changes(data):
  db.session.add(data)
  db.session.commit()