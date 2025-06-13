from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Product Management API',
          description='A simple product management API')

# Sample product data
products = [
    {"name": "Laptop", "price": 999, "description": "A powerful laptop for work and play."},
    {"name": "Smartphone", "price": 799, "description": "A cutting-edge smartphone."},
    {"name": "Headphones", "price": 199, "description": "Noise-cancelling headphones."}
]

# Define a model for product
product_model = api.model('Product', {
    'name': fields.String(required=True, description='Product name'),
    'price': fields.Float(required=True, description='Product price'),
    'description': fields.String(required=True, description='Product description')
})

# Create a namespace
ns = api.namespace('products', description='Product operations')

@ns.route('/')
class ProductList(Resource):
    @ns.doc('list_products')
    @ns.marshal_list_with(product_model)
    def get(self):
        """List all products"""
        return products

    @ns.doc('add_product')
    @ns.expect(product_model)
    @ns.marshal_with(product_model, code=201)
    def post(self):
        """Add a new product"""
        products.append(api.payload)
        return api.payload, 201

@ns.route('/<string:name>')
@ns.response(404, 'Product not found')
@ns.param('name', 'The product identifier')
class Product(Resource):
    @ns.doc('get_product')
    @ns.marshal_with(product_model)
    def get(self, name):
        """Fetch a product given its identifier"""
        for product in products:
            if product['name'] == name:
                return product
        api.abort(404)

    @ns.doc('update_product')
    @ns.expect(product_model)
    @ns.marshal_with(product_model)
    def put(self, name):
        """Update a product given its identifier"""
        for product in products:
            if product['name'] == name:
                product.update(api.payload)
                return product
        api.abort(404)

    @ns.doc('delete_product')
    @ns.response(204, 'Product deleted')
    def delete(self, name):
        """Delete a product given its identifier"""
        for product in products:
            if product['name'] == name:
                products.remove(product)
                return '', 204
        api.abort(404)

if __name__ == '__main__':
    app.run(debug=True)