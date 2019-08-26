from Models.finding_categories import FindingCategory
from app import db

def get_all_finding_categories():
  return FindingCategory.query.all()

def get_finding_category(id):
  category = FindingCategory.query.filter(FindingCategory.category_id == id).one()
  return category

def add_finding_category(data):
  new_category=FindingCategory(
    category_name=data.get('category_name'),
    category_severity = data.get('category_severity'),
    category_description = data.get('category_description'),
    category_remediation = data.get('category_remediation')
    )
  save_changes(new_category)
  return new_category
  
def update_category(data):
  save_changes(data)
  return data

def delete_finding_category(id):
  category = FindingCategory.query.filter(FindingCategory.category_id == id).one()
  db.session.delete(category)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()