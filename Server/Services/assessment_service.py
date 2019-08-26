from Models.assessments import Assessment
from app import db

def get_all_assessments():
  return Assessment.query.all()

def get_assessment(id):
  assessment = Assessment.query.filter(Assessment.assessment_id == id).one()
  return assessment

def add_assessment(data):
  new_assessment=Assessment(
    start_date=data.get('start_date'),
    completed_date = data.get('completed_date'),
    total_hours = data.get('total_hours'),
    invoice_id = data.get('invoice_id')
    )
  save_changes(new_assessment)
  return new_assessment

def delete_assessment(id):
  assessment = Assessment.query.filter(Assessment.assessment_id == id).one()
  db.session.delete(assessment)
  db.session.commit()
  
def update_assessment(data):
  save_changes(data)
  return data

def save_changes(data):
  db.session.add(data)
  db.session.commit()