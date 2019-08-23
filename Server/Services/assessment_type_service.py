from Models.assessment_types import AssessmentType
from app import db

def get_all_assessment_types():
  return AssessmentType.query.all()

def add_assessment_type(data):
  new_type=AssessmentType(assessment_type_name=data['assessment_type_name'])
  save_changes(new_type)
  return new_type
  
def update_assessment_type(data):
  save_changes(data)
  return data

def save_changes(data):
  db.session.add(data)
  db.session.commit()