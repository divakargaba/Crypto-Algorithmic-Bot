from flask import Blueprint, render_template

# Define the blueprint
main = Blueprint('main', __name__)

# Define routes
@main.route('/')
def index():
    return render_template('index.html')

