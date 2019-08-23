from app import db

class FindingCategory(db.Model):
  __tablename__='finding_categories'
  category_id = db.Column('category_id',db.Integer,primary_key=True)
  category_name = db.Column('category_name', db.String())
  category_severity = db.Column('category_severity', db.String())
  category_description = db.Column('category_description', db.String())
  category_remediation = db.Column('category_remediation', db.String())
  
  
