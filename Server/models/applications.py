from app import db

class Application(db.Model):
  __tablename__='applications'
  application_id = db.Column('application_id',db.Integer,primary_key=True)
  application_name = db.Column('application_name', db.String())
  customer_id = db.Column('customer_id', db.Integer, db.ForeignKey('customers.customer_id'))
  application_type = db.Column('application_type', db.String())

  def __init__(self, application_name, customer_id, application_type):
    self.application_name=application_name
    self.customer_id=customer_id
    self.application_type=application_type

  def __repr__(self):
    return '<id {}>'.format(self.application_id)