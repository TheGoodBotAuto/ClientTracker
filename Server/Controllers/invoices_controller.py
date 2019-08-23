from flask_restplus import Resource, Namespace
from flask import jsonify, request
from Models.invoices import Invoice
from Services.invoice_service import get_all_invoices,add_invoice, update_invoice
from Util.dto import InvoiceDto

api=InvoiceDto.api
model=InvoiceDto.model

# sanity check route
@api.route('/')
class InvoiceList(Resource):
  @api.marshal_with(model)
  @api.doc('List of invoices')
  def get(self):
    return get_all_invoices()

  @api.marshal_with(model)
  @api.expect(model)
  def post(self, app):
    data = request.json
    add_invoice(data)

@api.route('/<invoice_id>')
@api.param('invoice_id','Invoice id')
@api.response(404,'Invoice not found')
class Inv(Resource):
  @api.doc('Get Invoice info')
  @api.marshal_with(Invoice)
  def get(self, id):
    return jsonify('pong')

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')