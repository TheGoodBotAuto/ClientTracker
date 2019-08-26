from Models.findings import Finding
from app import db

def get_all_findings():
  return Finding.query.all()

def get_finding(id):
  finding = Finding.query.filter(Finding.finding_id == id).one()
  return finding

def add_finding(data):
  new_finding=Finding(
    finding_title=data.get('finding_title'),
    finding_category_id=data.get('finding_category_id'),
    finding_details=data.get('finding_details'),
    finding_severity=data.get('finding_severity'),
    recommended_fix=data.get('recommended_fix'),
    date_discovered=data.get('date_discovered'),
    date_remediated=data.get('date_remediated'),
    finding_comments=data.get('finding_comments')
    )
  save_changes(new_finding)
  return new_finding
  
def update_finding(data):
  save_changes(data)
  return data

def delete_finding(id):
  finding = Finding.query.filter(Finding.finding_id == id).one()
  db.session.delete(finding)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()