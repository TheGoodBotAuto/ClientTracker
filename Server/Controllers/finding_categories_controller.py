from flask_restplus import Resource, Namespace
from flask import jsonify, request
from Models.finding_categories import FindingCategory
from Util.dto import FindingCategoryDto
from Services.finding_category_service import get_all_finding_categories,add_finding_category,update_category

api=FindingCategoryDto.api
model=FindingCategoryDto.model

# sanity check route
@api.route('/')
class CategoryList(Resource):
  @api.marshal_with(model)
  @api.doc('List of finding categories')
  def get(self):
    return get_all_finding_categories()

  @api.marshal_with(model)
  @api.expect(model)
  def post(self, app):
    data=request.json
    return add_finding_category(data)

@api.route('/<category_id>')
@api.param('category_id','Finding Category id')
@api.response(404,'Finding Category not found')
class Category(Resource):
  @api.doc('Get Category info')
  @api.marshal_with(model)
  def get(self, id):
    return jsonify('pong')

@api.route('/healthcheck')
class healthCheck(Resource):
  def get(self):
    return jsonify('Ok!')