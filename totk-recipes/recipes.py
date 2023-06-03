from flask import Flask, render_template
import json
import sys
from os import path

app = Flask(__name__)

script_path = path.dirname(sys.argv[0])
with open(path.join(script_path, 'ingredients.json'), 'r') as ingredients_file:
    ingredients = json.load(ingredients_file)
with open(path.join(script_path, 'recipes.json'), 'r') as recipes_file:
    recipes = json.load(recipes_file)

@app.route('/')
def index():
    return render_template('recipes.html', ingredients=ingredients, recipes=recipes) # This knows to automatically look in the templates folder

if __name__ == "__main__":
    app.run(debug=True)
