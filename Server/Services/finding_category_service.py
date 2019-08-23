from Models.finding_categories import FindingCategory
from app import db

def get_all_finding_categories():
  return FindingCategory.query.all()

def add_finding_category(data):
  new_category=FindingCategory(
    category_name=data['contact_name'],
    category_severity = data['category_severity'],
    category_description = data['category_description'],
    category_remediation = data['category_remediation']
    )
  save_changes(new_category)
  return new_category
  
def update_category(data):
  save_changes(data)
  return data

def save_changes(data):
  db.session.add(data)
  db.session.commit()