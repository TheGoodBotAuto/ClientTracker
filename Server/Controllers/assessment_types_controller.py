from flask_restplus import Resource, Namespace
from flask import jsonify, request
from Util.dto import AssessmentTypeDto
from Services.assessment_type_service import get_all_assessment_types, add_assessment_type, update_assessment_type

api= AssessmentTypeDto.api
model = AssessmentTypeDto.model
# sanity check route
@api.route('/')
class TypeList(Resource):
  @api.marshal_with(model)
  @api.doc('List of assessment types')
  def get(self):
    return get_all_assessment_types()

  @api.marshal_with(model)
  @api.expect(model)
  def post(self):
    data = request.json
    return add_assessment_type(data)

@api.route('/<assessmenttype_id>')
@api.param('assessmenttype_id','Assessment Type id')
@api.response(404,'Assessment Type not found')
class Type(Resource):
  @api.doc('Get Assessment Type info')
  @api.marshal_with(model)
  def get(self, id):
    return jsonify('pong')

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')