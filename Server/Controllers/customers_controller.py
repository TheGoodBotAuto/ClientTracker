from flask_restplus import Resource, Namespace
from flask import jsonify, request
from Util.dto import CustomerDto
from Services.customer_service import get_all_customers, add_customer, delete_customer, get_customer

api = CustomerDto.api
model = CustomerDto.model
# sanity check route
@api.route('/')
class CustomerList(Resource):
  @api.marshal_list_with(model)
  @api.doc('List of Customers')
  def get(self):
    return get_all_customers()

  @api.marshal_with(model)
  @api.expect(model)
  def post(self):
    data= request.json
    return add_customer(data)

@api.route('/<customer_id>')
@api.param('customer_id','Customer id')
@api.response(404,'Customer not found')
class Cli(Resource):
  @api.doc('Get Customer info')
  @api.marshal_with(model)
  def get(self, customer_id):
    return get_customer(customer_id)
  @api.doc('Delete Customer info')
  @api.marshal_with(model)
  def delete(self, customer_id):
    return delete_customer(customer_id)

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')