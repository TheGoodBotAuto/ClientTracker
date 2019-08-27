from flask_restplus import Resource, Namespace
from flask import jsonify, request
from Util.dto import AssessmentTypeDto
from Services.assessment_type_service import get_all_assessment_types, get_assessment_type, add_assessment_type, update_assessment_type, delete_assessment_type

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
  def get(self, assessmenttype_id):
    assessment = get_assessment_type(assessmenttype_id)
    if not assessment:
      api.abort(404)
    else:
      return assessment
  
  @api.doc('Delete Assessment Type info')
  @api.marshal_with(model)
  def delete(self, assessmenttype_id):
    return delete_assessment_type(assessmenttype_id)

  @api.doc('Update Assessment Type info')
  @api.marshal_with(model)
  def post(self, assessmenttype_id):
    data = request.json
    return update_assessment_type(assessmenttype_id,data)

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')