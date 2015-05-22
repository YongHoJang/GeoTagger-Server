from flask import render_template, Blueprint


# Define the blueprint
facade_views = Blueprint('facade', __name__, template_folder='templates',
    static_folder='static')
    

@facade_views.route('/')
def index():
    return render_template('index.html')  