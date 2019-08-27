from Models.finding_categories import FindingCategory
from app import db

def get_all_finding_categories():
  return FindingCategory.query.all()

def get_finding_category(id):
  category = FindingCategory.query.filter(FindingCategory.category_id == id).first()
  return category

def add_finding_category(data):
  new_category=populate_fields(FindingCategory(),data)
  save_changes(new_category)
  return new_category
  
def update_finding_category(id,data):
  category = FindingCategory.query.filter(FindingCategory.category_id == id).first()
  if category:
    populate_fields(category,data)
    save_changes(category)
  return category

def populate_fields(category, data):
  category.category_name=data.get('category_name',category.category_name)
  category.category_severity=data.get('category_severity', category.category_severity)
  category.category_description=data.get('category_description',category.category_description)
  category.category_remediation=data.get('category_remediation',category.category_remediation)
  return category

def delete_finding_category(id):
  category = FindingCategory.query.filter(FindingCategory.category_id == id).first()
  db.session.delete(category)
  db.session.commit()

def save_changes(data):
  db.session.add(data)
  db.session.commit()