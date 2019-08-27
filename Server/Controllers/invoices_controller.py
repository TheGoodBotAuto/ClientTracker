from flask_restplus import Resource, Namespace
from flask import jsonify, request
from Models.invoices import Invoice
from Services.invoice_service import get_all_invoices,add_invoice, update_invoice, get_invoice, delete_invoice
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
  def post(self):
    data = request.json
    return add_invoice(data)

@api.route('/<invoice_id>')
@api.param('invoice_id','Invoice id')
@api.response(404,'Invoice not found')
class Inv(Resource):
  @api.doc('Get Invoice info')
  @api.marshal_with(model)
  def get(self, invoice_id):
    invoice= get_invoice(invoice_id)
    if not invoice:
      api.abort(404)
    else:
      return invoice


  def delete(self, invoice_id):
    return delete_invoice(invoice_id)

  @api.doc('Update Invoice info')
  @api.marshal_with(model)
  def post(self, invoice_id):
    data=request.json
    return update_invoice(invoice_id,data)

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')