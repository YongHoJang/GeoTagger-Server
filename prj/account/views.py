from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from flask import current_app
from models import User

account_views = Blueprint('account', __name__, template_folder='templates')


@account_views.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    if request.method == 'POST':
        # Create an user object & register
        
        # If email validation is required, send email to the user.
        
        pass

    return render_template('signup.html')
    

@account_views.route('/testuser', methods=['GET'])
def testuser():
    if request.method == 'GET':
        new_user = User.create('tester3','easyas123','Min','Seong','Kang',
            'tester@email.com')
        if new_user == None:
            return "The test user already exists!"
        new_user.save()
    return "Created a test user"
    
@account_views.route('/testanotheruser', methods=['GET'])
def testanother():
    if request.method == 'GET':
        new_user = User.get_with_username('tester3')
        if new_user == None:
            return "The test user already exists!"
        new_user.save()
    return "Created a test user"
        

@account_views.route('/')
def home():
    return 'Hello from account'