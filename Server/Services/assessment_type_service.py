from Models.assessment_types import AssessmentType
from app import db

def get_all_assessment_types():
  return AssessmentType.query.all()

def get_assessment_type(id):
  return AssessmentType.query.filter(AssessmentType.assessment_type_id == id).one()

def add_assessment_type(data):
  new_type=AssessmentType(assessment_type_name=data.get('assessment_type_name'))
  save_changes(new_type)
  return new_type
  
def update_assessment_type(data):
  save_changes(data)
  return data

def delete_assessment_type(id):
  assessment_type = AssessmentType.query.filter(AssessmentType.assessment_type_id == id).one()
  db.session.delete(assessment_type)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()