from flask_restplus import Resource, Namespace, fields
from flask import jsonify, request
from Util.dto import ApplicationDto
from Services.application_service import get_all_applications,add_application,update_application

api=ApplicationDto.api
model=ApplicationDto.model


# sanity check route
@api.route('/')
class AppList(Resource):
  @api.marshal_with(model)
  @api.doc('List of applications')
  def get(self):
    return get_all_applications()

  @api.marshal_with(model)
  @api.expect(model)
  def post(self, app):
    data = request.json
    return add_application(data)

@api.route('/<app_id>')
@api.param('app_id','Application id')
@api.response(404,'App not found')
class App(Resource):
  @api.doc('Get Application info')
  @api.marshal_with(model)
  def get(self, id):
    return jsonify('pong')

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')