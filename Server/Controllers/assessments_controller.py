from flask_restplus import Resource, Namespace
from flask import jsonify, request
from Models.assessments import Assessment
from Util.dto import AssessmentDto
from Services.assessment_service import get_all_assessments,add_assessment,update_assessment, get_assessment, delete_assessment

api=AssessmentDto.api
model=AssessmentDto.model

# sanity check route
@api.route('/')
class AssessmentList(Resource):
  @api.marshal_with(model)
  @api.doc('List of assessments')
  def get(self):
    return get_all_assessments()

  @api.marshal_with(model)
  @api.expect(model)
  def post(self):
    data = request.json
    return add_assessment(data)

@api.route('/<assessment_id>')
@api.param('assessment_id','Assessment id')
@api.response(404,'Assessment not found')
class Assess(Resource):
  @api.doc('Get Assessment info')
  @api.marshal_with(model)
  def get(self, assessment_id):
    return get_assessment(assessment_id)

  def delete(self, assessment_id):
    return delete_assessment(assessment_id)

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')