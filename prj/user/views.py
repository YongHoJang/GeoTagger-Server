from flask import Blueprint, render_template, abort, request, redirect, flash
from flask import url_for
from jinja2 import TemplateNotFound
from flask import current_app
from models import User, Project
from forms import RegistrationForm, RecaptchaRegistrationForm, LoginForm
from forms import ChangePasswordForm, CreateProjectForm
from flask.ext.login import login_user, login_required
from flask.ext.login import logout_user, current_user
from flask.ext.mail import Message, Mail
from settings import RECAPTCHA_ENABLED
from bson.objectid import ObjectId


user_views = Blueprint('user', __name__, template_folder='templates',
    static_folder='static')


@user_views.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    
    if RECAPTCHA_ENABLED:
        form = RecaptchaRegistrationForm(request.form)
    else:
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
    
    
@user_views.route('/login', methods=['GET','POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # login and validate the user...
        email = form.email.data
        password = form.password.data
        user = User.get_with_username(email)

        if user and user.is_active() and not user.is_anonymous():
            if user.authenticate(password):
                login_user(user)
                flash("Logged in successfully.")
                return redirect(request.args.get("next") or url_for(".index"))
            else:
                error = "Your username or password is not valid"
        
    return render_template("login.html", form=form, error=error)


@user_views.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('logout.html')  
    

@user_views.route('/')
@login_required
def index():
    firstname = current_user.firstname
    lastname = current_user.lastname
    return render_template("index.html", firstname=firstname, lastname=lastname)


@user_views.route('/emailappkey')
@login_required
def email_appkey():
    # Get user info
    # generate new key and send it in email
    new_appkey = current_user.generate_appkey()
    current_user.save()
    # Email new appkey
    mail = Mail(current_app._get_current_object())
    message = Message("Your new appkey for 4k mobile app",
        sender='fourkayproject@gmail.com',
        recipients=[current_user.email])
    message.body = ('Your New Appkey: %s' % new_appkey)
    mail.send(message)
    flash("New appkey has been send to your email.", category='index_page')
    return redirect(url_for('.index'))


@user_views.route('/verifyemailappkey')
@login_required
def verify_email_appkey():
    return render_template("verify_email_appkey.html")


@user_views.route('/changepassword', methods=['GET','POST'])
@login_required
def change_password():
    '''
    Change a user's password
    '''
    form = ChangePasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        if current_user.check_password(form.old_password.data):
            current_user.update_password(form.new_password.data)
            current_user.save()
            flash("Your password has been updated.", category='index_page')
            return redirect(url_for('.index'))
        else:
            flash("Your password does not match.", category='error')
            return render_template('change_password.html', form=form)    
    return render_template('change_password.html', form=form)


@user_views.route('/createproject', methods=['GET','POST'])
@login_required
def create_project():
    form = CreateProjectForm(request.form)
    
    if request.method == 'POST' and form.validate():
        project = Project(prj_name=form.name, prj_desc=form.desc, 
            owner=current_user._id)
        project.save()
        flash("New project has been created.", category='index_page')
        return redirect(url_for('.index'))
        
    return render_template('create_project.html', form=form)
    

# TODO: Delete test methods
#
@user_views.route('/testuser', methods=['GET'])
def testuser():
    if request.method == 'GET':
        # Check if the user exists.
        username = 'tester1@email.com'
        email = username
        new_user = User.get_with_username(username)
        if new_user is not None:
            return "The test user already exists!"
            
        new_user = User.create(username,'easyas123','Min','Seong','Kang',
            email)
        new_user.active = True
        new_user.save()
    return "Created a test user"
    
    
@user_views.route('/testanotheruser', methods=['GET'])
def testanother():
    if request.method == 'GET':
        new_user = User.get_with_username('tester3')
        if new_user == None:
            return "The test user already exists!"
        new_user.save()
    return "Created a test user"
        

