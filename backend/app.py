from flask import Flask, request, jsonify , send_file, send_from_directory
from flask_cors import CORS
import sqlite3
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'  # Use SQLite URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200))
    cooking_time = db.Column(db.String(100))
    
    def __init__(self, name, ingredients, cooking_time, image_filename=None):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.image_path = image_filename


        

@app.route('/')
@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    recipe_list = []
    for recipe in recipes:
        recipe_list.append({
            'id': recipe.id,
            'name': recipe.name,
            'ingredients': recipe.ingredients,
            'cooking_time': recipe.cooking_time
        })
        total_recipes = jsonify({'recipes': recipe_list})
    return send_file(total_recipes , 'C:\\Users\\user\\Desktop\\coding fullstack\\cousre1.1\\HW13+14\\HW14\\API recipes\\frontend\\index.html')


# Add a new recipe
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    data = request.get_json()
    new_recipe = Recipe(
        name=data['name'],
        ingredients=data['ingredients'],
        cooking_time=data['cooking_time']
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe added successfully'})

# Edit a recipe
@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe is None:
        return jsonify({'error': 'Recipe not found'}), 404
    
    data = request.get_json()
    recipe.name = data.get('name', recipe.name)
    recipe.ingredients = data.get('ingredients', recipe.ingredients)
    recipe.cooking_time = data.get('cooking_time', recipe.cooking_time)
    
    db.session.commit()
    return jsonify({'message': 'Recipe updated successfully'})

# Delete a recipe
@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if recipe is None:
        return jsonify({'error': 'Recipe not found'}), 404
    
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'message': 'Recipe deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=9000)