from flask_restplus import Resource, Namespace
from flask import jsonify, request
from Models.contacts import Contact
from Util.dto import ContactDto
from Services.contact_service import get_all_contacts, add_contact,update_contact

api=ContactDto.api
model=ContactDto.model

# sanity check route
@api.route('/')
class ContactList(Resource):
  @api.marshal_with(model)
  @api.doc('List of contacts')
  def get(self):
    return get_all_contacts()

  @api.marshal_with(model)
  @api.expect(model)
  def post(self, app):
    data = request.json
    return add_contact(data)

@api.route('/<contact_id>')
@api.param('contact_id','Contact id')
@api.response(404,'Contact not found')
class Cont(Resource):
  @api.doc('Get Contact info')
  @api.marshal_with(model)
  def get(self, id):
    return jsonify('pong')

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')