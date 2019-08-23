from flask_restplus import Api, Resource
from .customers_controller import api as ns1
from .applications_controller import api as ns2
from .invoices_controller import api as ns3
from .finding_categories_controller import api as ns4
from .findings_controller import api as ns5
from .contacts_controller import api as ns6
from .assessments_controller import api as ns7
from .assessment_types_controller import api as ns8
from flask import Blueprint, jsonify

def createBlueprint():
  blueprint = Blueprint('api',__name__)
  api = Api(blueprint, doc='/docs')

  @api.route('/healthcheck', methods=['GET'])
  class healthcheck(Resource):
    def get(self):
      return jsonify('Ok!')
  api.add_namespace(ns1)
  api.add_namespace(ns2)
  api.add_namespace(ns3)
  api.add_namespace(ns4)
  api.add_namespace(ns5)
  api.add_namespace(ns6)
  api.add_namespace(ns7)
  api.add_namespace(ns8)

  return blueprint

