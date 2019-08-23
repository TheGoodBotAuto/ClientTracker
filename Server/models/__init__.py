from .applications import Application
from .assessment_types import AssessmentType
from .assessments import Assessment
from .contacts import Contact
from .customers import Customer
from .finding_categories import FindingCategory
from .findings import Finding
from .invoices import Invoice


__all__=['Application','AssessmentType','Assessment','Contact','Customer','FindingCategory','Finding','Invoice']

def createDatabase(app):
  db = SQLAlchemy(app)