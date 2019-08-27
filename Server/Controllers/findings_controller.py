from flask_restplus import Resource, Namespace
from flask import jsonify, request
from Models.findings import Finding
from Util.dto import FindingDto
from Services.finding_service import get_all_findings, add_finding,update_finding, get_finding, delete_finding

api=FindingDto.api
model=FindingDto.model

# sanity check route
@api.route('/')
class FindingList(Resource):
  @api.marshal_with(model)
  @api.doc('List of findings')
  def get(self):
    return get_all_findings()

  @api.marshal_with(model)
  @api.expect(model)
  def post(self):
    data = request.json
    return add_finding(data)

@api.route('/<finding_id>')
@api.param('finding_id','Finding id')
@api.response(404,'Finding not found')
class Find(Resource):
  @api.doc('Get Finding info')
  @api.marshal_with(model)
  def get(self, finding_id):
    finding = get_finding(finding_id)
    if not finding:
      api.abort(404)
    else:
      return finding

  def delete(self, finding_id):
    return delete_finding(finding_id)

  @api.doc('Update Finding info')
  @api.marshal_with(model)
  def post(self, finding_id):
    data=request.json
    return update_finding(finding_id,data)

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')