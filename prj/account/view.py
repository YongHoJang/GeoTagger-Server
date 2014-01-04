from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound


website = Blueprint('website', __name__, template_folder='templates')


@website.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    if request.method == 'POST':
        pass

    return render_template('signup.html')