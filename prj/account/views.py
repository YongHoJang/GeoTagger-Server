from flask import Blueprint, render_template, abort, request, redirect, flash
from flask import url_for
from jinja2 import TemplateNotFound
from flask import current_app
from models import User
from forms import RegistrationForm, LoginForm
from flask.ext.login import LoginManager, login_user, login_required
from flask.ext.login import logout_user, current_user

account_views = Blueprint('account', __name__, template_folder='templates')



@account_views.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
        #                   form.password.data)
        #       db_session.add(user)
        user = User.create(username=form.email.data, email=form.email.data,
            firstname=form.firstname.data, middlename=form.middlename.data, 
            lastname=form.lastname.data, password=form.password.data)
        if user is not None:
            user.save()
            flash('Thanks for registering')
            # TODO: Send a validation email.
            return render_template('signup_done.html')
        else:
            error = 'Your email has been already used! Use new email address.'
            
    return render_template('signup.html', form=form, error=error)
    
    
@account_views.route('/login', methods=['GET','POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if form.validate_on_submit():
        # login and validate the user...
        email = form.email.data
        password = form.password.data
        user = User.get_with_username(email)
        print 'hi'
        print 'active:', user.is_active()
        if user and user.is_active() and not user.is_anonymous():
            if user.authenticate(password):
                login_user(user)
                flash("Logged in successfully.")
                print 'you logged in'
                return redirect(request.args.get("next") or url_for(".index"))
            else:
                error = "Your username or password is not valid"
        
    return render_template("login.html", form=form, error=error)


@account_views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')  
    

@account_views.route('/')
@login_required
def index():
    firstname = current_user.firstname
    lastname = current_user.lastname
    print 'fistname', firstname
    return render_template("index.html", firstname=firstname, lastname=lastname)


# TODO: Delete test methods
#
@account_views.route('/testuser', methods=['GET'])
def testuser():
    if request.method == 'GET':
        # Check if the user exists.
        username = 'tester@email.com'
        email = username
        new_user = User.get_with_username(username)
        if new_user is not None:
            return "The test user already exists!"
            
        new_user = User.create(username,'easyas123','Min','Seong','Kang',
            email)
        new_user.active = True
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
        

