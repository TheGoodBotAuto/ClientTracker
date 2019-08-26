from flask_restplus import Resource, Namespace, fields
from flask import jsonify, request
from Util.dto import ApplicationDto
from Services.application_service import get_all_applications,add_application,update_application, delete_application,get_application

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
  def post(self):
    data = request.json
    return add_application(data)

@api.route('/<app_id>')
@api.param('app_id','Application id')
@api.response(404,'App not found')
class App(Resource):
  @api.doc('Get Application info')
  @api.marshal_with(model)
  def get(self, app_id):
    return get_application(app_id)

  def delete(self,app_id):
    return delete_application(app_id)

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')