from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample product data
products = [
    {"name": "Laptop", "price": 999, "description": "A powerful laptop for work and play."},
    {"name": "Smartphone", "price": 799, "description": "A cutting-edge smartphone."},
    {"name": "Headphones", "price": 199, "description": "Noise-cancelling headphones."}
]

@app.route('/')
def home():
    # Passing the products data to the template
    return render_template('index.html', products=products)

@app.get('/data')
def data():
    # Passing the products data to the template
    return jsonify(products)

# Update the product data
@app.put('/update_product/<string:name>')
def update_product(name):
    request_update_product = request.get_json()
    for product in products:
        if product['name'] == name:
            product.update(request_update_product)
            return jsonify(product)
    return jsonify({'message': 'Product not found'}), 404

@app.post('/add_product')
def add_product():
    request_add_product = request.get_json()
    products.append(request_add_product)
    return jsonify(products)

# Remove product by name
@app.delete('/remove_product/<string:name>')
def remove_product(name):
    for product in products:
        if product['name'] == name:
            products.remove(product)
            return jsonify(products)
    return jsonify({'message': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
