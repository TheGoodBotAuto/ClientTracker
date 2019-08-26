from flask_restplus import Namespace, fields


class ApplicationDto:
  api= Namespace('applications', description='Applications')
  model=api.model('application', {
    'application_id': fields.Integer(),
    'application_name': fields.String(),
    'customer_id': fields.Integer(),
    'application_type': fields.String()
  })

class AssessmentDto:
  api= Namespace('assessments', description='Assessments')
  model=api.model('assessment', {
    'assessment_id': fields.Integer(),
    'start_date': fields.DateTime(),
    'completed_date': fields.DateTime(),
    'total_hours': fields.Float(),
    'invoice_id': fields.Integer()
  })

class AssessmentTypeDto:
  api= Namespace('assessmenttypes', description='assessmenttypes')
  model=api.model('assessmenttype', {
    'assessment_type_id': fields.Integer(),
    'assessment_type_name': fields.String()
  })

class CustomerDto:
  api= Namespace('customers', description='Customers')
  model=api.model('customer', {
    'customer_id': fields.Integer(),
    'customer_name': fields.String()
  })

class ContactDto:
  api= Namespace('contacts', description='Contacts')
  model=api.model('contacts', {
    'contact_id': fields.Integer(),
    'contact_name': fields.String(),
    'contact_email': fields.String(),
    'contact_phone': fields.String(),
    'application_id': fields.Integer(),
    'customer_id': fields.Integer()
  })

class FindingCategoryDto:
  api= Namespace('findingcategories', description='Contacts')
  model=api.model('contacts', {
    'category_id': fields.Integer(),
    'category_name': fields.String(),
    'category_severity': fields.String(),
    'category_description': fields.String(),
    'category_remediation': fields.String()
  })

class FindingDto:
  api= Namespace('findings', description='Findings')
  model=api.model('findings', {
    'finding_id': fields.Integer(),
    'finding_title': fields.String(),
    'finding_category_id': fields.Integer(),
    'finding_details': fields.String(),
    'finding_severity': fields.String(),
    'recommended_fix': fields.String(),
    'date_discovered': fields.DateTime(),
    'date_remediated': fields.DateTime(default=None),
    'finding_comments': fields.String()
  })

class InvoiceDto:
  api= Namespace('invoices', description='Invoices')
  model=api.model('invoices', {
    'invoice_id': fields.Integer(),
    'invoice_number': fields.Integer(),
    'customer_id': fields.Integer(),
    'hourly_rate': fields.Float(),
    'amount_billed': fields.Float(),
    'description_of_service': fields.String(),
    'invoice_paid_date': fields.DateTime()
  })
