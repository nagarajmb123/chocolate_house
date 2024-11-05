# app.py
from flask import Flask, request, jsonify ,render_template
from models import seasonal_flavors, ingredients, customer_suggestions

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# Welcome Route
@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to the Chocolate House!"

# Seasonal Flavors Routes
@app.route('/flavors', methods=['GET'])
def get_flavors():
    flavors = seasonal_flavors.get_flavors()
    return jsonify(flavors)

@app.route('/flavors', methods=['POST'])
def add_flavor():
    data = request.json
    seasonal_flavors.add_flavor(data['flavor_name'], data['description'])
    return jsonify({"message": "Flavor added successfully"}), 201

# Ingredients Routes
@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    ingredients_list = ingredients.get_ingredients()
    return jsonify(ingredients_list)

@app.route('/ingredients', methods=['POST'])
def add_ingredient():
    data = request.json
    ingredients.add_ingredient(data['ingredient_name'], data['quantity'])
    return jsonify({"message": "Ingredient added successfully"}), 201

# Customer Suggestions Routes
@app.route('/suggestions', methods=['GET'])
def get_suggestions():
    suggestions = customer_suggestions.get_suggestions()
    return jsonify(suggestions)

@app.route('/suggestions', methods=['POST'])
def add_suggestion():
    data = request.json
    customer_suggestions.add_suggestion(data['customer_name'], data['suggestion'], data['allergy_concern'])
    return jsonify({"message": "Suggestion added successfully"}), 201

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Test route reached!"})


if __name__ == '__main__':
    app.run(debug=True)
