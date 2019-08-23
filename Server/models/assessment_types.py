from app import db

class AssessmentType(db.Model):
  __tablename__='assessment_types'
  assessment_type_id = db.Column('assessment_type_id',db.Integer,primary_key=True)
  assessment_type_name = db.Column('assessment_type_name', db.String())
  