from app import db

class AssessmentTypes(db.Model):
  __tablename__='assessment_types'
  assessment_type_id = db.Column(db.Integer,primary_key=True)
  assessment_type_name = db.Column('assessment_type_name', db.String())
  