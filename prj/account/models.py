import json
import string
import random
from flask.ext.login import UserMixin
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId



# Configuration Parameters
# ------------------------
encryption_method = 'pbkdf2:sha256:5000'


class User(UserMixin):
    '''
    User object that will be managed by Flask-Login and work with MongoDB
    '''
    def __init__(self, username, firstname, middlename, lastname, email, 
        active, anonymous, validated, userid='', password_hash=''):   
        self.active = active
        self.anonymous = anonymous
        self.validated = validated
        self.username = username
        self.password_hash = password_hash
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.email = email
        self.password_hash = password_hash
        self.userid = userid
        self.appkey = self.generate_appkey()
    
    
    def authenticate(self, password):
        # if password is same with password in db
        # set self.authenticated = True
        return check_password_hash(self.password_hash, password)
            
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        

    def generate_appkey(self):
        key_length = 8
        key_chars = string.ascii_lowercase + string.digits
        appkey = ''.join(random.choice(key_chars) for x in range(key_length))
        return appkey
    
        
    def save(self):
        mongo = current_app._get_current_object().data.driver
        obj_str = json.dumps(self, default=lambda o: o.__dict__)
        obj = json.loads(obj_str)
        #print 'new user json is: %s' % obj_str
        mongo.db.accounts.update({'username':self.username},obj, upsert=True)
        
        
        
    @staticmethod
    def create(username, password, firstname, middlename, lastname, email):
        mongo = current_app._get_current_object().data.driver
        # To check if username is already existing.
        user = mongo.db.accounts.find_one({'username': username})
        if user:
            return None # the username is already existing. Throw an exception.
        else:
            # Generate a salted password by using PBKDF2-SHA256
            password_hash = generate_password_hash(password, 
                method=encryption_method)
           
            new_user = User(username=username, password_hash=password_hash,
                firstname=firstname, middlename=middlename, lastname=lastname,
                email=email, active=False, anonymous=False,
                validated=False)
        
            return new_user       
        
        
    @staticmethod
    def get_with_username(username=''):
        '''
        Return User object that matches a given username by reading a db.
        This method should be called inside of request context in order to get
        current_app object.
        '''
        mongo = current_app._get_current_object().data.driver
        user = mongo.db.accounts.find_one({'username': username})
        
        if user is None:
            return None
        
        return User(username=user['username'], userid=str(user['_id']), 
            firstname=user['firstname'], middlename=user['middlename'],
            lastname=user['lastname'], email=user['email'],
            password_hash=user['password_hash'], 
            validated=user['validated'], active=user['active'], 
            anonymous=False)
            
            
    @staticmethod
    def get_with_userid(userid):
        mongo = current_app._get_current_object().data.driver
        print 'userid is:', userid
        user = mongo.db.accounts.find_one({'_id': ObjectId(userid)})
        print 'user is:', user
        return User.get_with_username(username=user['username'])
        
                
    # methods for Flask-Login user
    # ===
    def is_authenticated(self):
        ''' Assume all User object after login point are authenticated. 
            That means that if you have User ID stored in user session,
            it is authenticated.
        '''
        return True
        
    def is_active(self):
        return self.active
    
        
    def is_anonymous(self):
        return self.anonymous
    
    
    def get_id(self):
        return self.userid        
        
        
        
    
    
    
    