# app.py
from flask import Flask, request, jsonify ,render_template
from models import seasonal_flavors, ingredients, customer_suggestions

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
#this route is for welcome to the application
@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to the Chocolate House!"

#this route is to get the seasonalFlavors
@app.route('/flavors', methods=['GET'])
def getSeasonalFlavors():
    flavors = seasonal_flavors.getSeasonalFlavors()
    return jsonify(flavors)

#this route is to add seasonalFlavors
@app.route('/flavors', methods=['POST'])
def addingSeasonalFlavors():
    data = request.json
    seasonal_flavors.addingSeasonalFlavors(data['flavor_name'], data['description'])
    return jsonify({"message": "Flavor added successfully"}), 201

#this route is to get ingredients
@app.route('/ingredients', methods=['GET'])
def getAllIngredients():
    ingredientslist = ingredients.getAllIngredients()
    return jsonify(ingredientslist)

#this route is to add ingredients
@app.route('/ingredients', methods=['POST'])
def addingIngredient():
    data = request.json
    ingredients.addingIngredient(data['ingredient_name'], data['quantity'])
    return jsonify({"message": "Ingredient added successfully"}), 201

#this route is to get customersuggestions
@app.route('/suggestions', methods=['GET'])
def getALLSuggestions():
    Suggestion = customer_suggestions.getALLSuggestions()
    return jsonify(Suggestion)
#this route is to add customersuggestions
@app.route('/suggestions', methods=['POST'])
def addingSuggestion():
    data = request.json
    customer_suggestions.addingSuggestion(data['customer_name'], data['suggestion'], data['allergy_concern'])
    return jsonify({"message": "Suggestion added successfully"}), 201




if __name__ == '__main__':
    app.run(debug=True)
