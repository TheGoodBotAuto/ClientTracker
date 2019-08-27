from Models.assessments import Assessment
from app import db

def get_all_assessments():
  return Assessment.query.all()

def get_assessment(id):
  assessment = Assessment.query.filter(Assessment.assessment_id == id).first()
  return assessment

def add_assessment(data):
  new_assessment=populate_fields(Assessment(),data)
  save_changes(new_assessment)
  return new_assessment

def delete_assessment(id):
  assessment = Assessment.query.filter(Assessment.assessment_id == id).first()
  db.session.delete(assessment)
  db.session.commit()
  
def update_assessment(id,data):
  assessment = Assessment.query.filter(Assessment.assessment_id == id).first()
  if assessment:
    populate_fields(assessment,data)
    save_changes(assessment)
  return assessment

def populate_fields(assessment, data):
  assessment.start_date=data.get('start_date',assessment.start_date)
  assessment.completed_date=data.get('completed_date',assessment.completed_date)
  assessment.total_hours=data.get('total_hours',assessment.total_hours)
  assessment.invoice_id=data.get('invoice_id',assessment.invoice_id)
  return assessment

def save_changes(data):
  db.session.add(data)
  db.session.commit()