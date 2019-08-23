from app import db

class Finding(db.Model):
  __tablename__='findings'
  finding_id = db.Column('finding_id',db.Integer,primary_key=True)
  finding_title = db.Column('finding_title', db.String())
  finding_category_id = db.Column('finding_category_id', db.Integer, db.ForeignKey('finding_categories.category_id'))
  finding_details = db.Column('finding_details', db.String())
  finding_severity = db.Column('finding_severity', db.String())
  recommended_fix = db.Column('recommended_fix', db.String())
  date_discovered = db.Column('date_discovered', db.Date)
  date_remediated = db.Column('date_remediated', db.Date)
  finding_comments = db.Column('finding_comments', db.String())
