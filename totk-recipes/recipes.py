from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)

with open('ingredients.json', 'r') as ingredients_file:
    ingredients = json.load(ingredients_file)
with open('recipes.json', 'r') as recipes_file:
    recipes = json.load(recipes_file)

@app.route('/')
def index():
    return render_template('recipes.html', ingredients=ingredients, recipes=recipes) # This knows to automatically look in the templates folder

if __name__ == "__main__":
    app.run(debug=True)
