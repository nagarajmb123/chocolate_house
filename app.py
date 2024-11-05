# app.py
from flask import Flask, request, jsonify, render_template
from models import seasonal_flavors, ingredients, customer_suggestions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#to get all Seasonal flavors 
@app.route('/flavors', methods=['GET'])
def get_flavors():
    flavors = seasonal_flavors.get_flavors()
    return jsonify(flavors)
#to add seasonal flavour
@app.route('/flavors', methods=['POST'])
def add_flavor():
    data = request.json
    seasonal_flavors.add_flavor(data['flavor_name'], data['description'])
    return jsonify({"message": "Flavor added successfully"}), 201
#to delete 
@app.route('/flavors/<int:flavor_id>', methods=['DELETE'])
def delete_flavor(flavor_id):
    seasonal_flavors.delete_flavor(flavor_id)
    return jsonify({"message": "Flavor deleted successfully"}), 204

#to get all Ingredients 
@app.route('/ingredients', methods=['GET'])
def get_ingredients():
    ingredients_list = ingredients.get_ingredients()
    return jsonify(ingredients_list)
#to add Ingredients
@app.route('/ingredients', methods=['POST'])
def add_ingredient():
    data = request.json
    ingredients.add_ingredient(data['ingredient_name'], data['quantity'])
    return jsonify({"message": "Ingredient added successfully"}), 201
#to delete Ingredients
@app.route('/ingredients/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(ingredient_id):
    ingredients.delete_ingredient(ingredient_id)
    return jsonify({"message": "Ingredient deleted successfully"}), 204

#CustomerSuggestions 
#to get all CustomerSuggestions 
@app.route('/suggestions', methods=['GET'])
def get_suggestions():
    suggestions = customer_suggestions.get_suggestions()
    return jsonify(suggestions)
#to add CustomerSuggestions
@app.route('/suggestions', methods=['POST'])
def add_suggestion():
    data = request.json
    customer_suggestions.add_suggestion(data['customer_name'], data['suggestion'], data['allergy_concern'])
    return jsonify({"message": "Suggestion added successfully"}), 201
#to delete CustomerSuggestions
@app.route('/suggestions/<int:suggestion_id>', methods=['DELETE'])
def delete_suggestion(suggestion_id):
    customer_suggestions.delete_suggestion(suggestion_id)
    return jsonify({"message": "Suggestion deleted successfully"}), 204

if __name__ == '__main__':
    app.run(debug=True)
