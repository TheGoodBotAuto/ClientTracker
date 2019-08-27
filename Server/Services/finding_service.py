from Models.findings import Finding
from app import db

def get_all_findings():
  return Finding.query.all()

def get_finding(id):
  finding = Finding.query.filter(Finding.finding_id == id).first()
  return finding

def add_finding(data):
  new_finding=populate_fields(Finding(),data)
  save_changes(new_finding)
  return new_finding
  
def update_finding(id,data):
  finding = Finding.query.filter(Finding.finding_id == id).first()
  if finding:
    populate_fields(finding,data)
    save_changes(finding)
  return finding

def populate_fields(finding, data):
  finding.finding_title=data.get('finding_title',finding.finding_title)
  finding.finding_category_id=data.get('finding_category_id',finding.finding_category_id)
  finding.finding_details=data.get('finding_details',finding.finding_details)
  finding.finding_severity=data.get('finding_severity',finding.finding_severity)
  finding.recommended_fix=data.get('recommended_fix',finding.recommended_fix)
  finding.date_discovered=data.get('date_discovered',finding.date_discovered)
  finding.date_remediated=data.get('date_remediated',finding.date_remediated)
  finding.finding_comments=data.get('finding_comments',finding.finding_comments)
  return finding

def delete_finding(id):
  finding = Finding.query.filter(Finding.finding_id == id).first()
  db.session.delete(finding)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()