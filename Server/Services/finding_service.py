from Models.findings import Finding
from app import db

def get_all_findings():
  return Finding.query.all()

def add_finding(data):
  new_finding=Finding(finding_name=data['finding_name'])
  save_changes(new_finding)
  return new_finding
  
def update_finding(data):
  save_changes(data)
  return data

def save_changes(data):
  db.session.add(data)
  db.session.commit()