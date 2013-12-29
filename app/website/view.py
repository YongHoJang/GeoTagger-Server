from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from settings import mongodb as mongo

website = Blueprint('website', __name__,
                        template_folder='templates')



@website.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    if request.method == 'POST':
        pass
    #user = mongo.accounts.find_one({'username':'tester'})
    return render_template('signup.html')