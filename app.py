from flask import Flask, render_template, jsonify

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

@app.route('/data')
def data():
    # Passing the products data to the template
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
