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
    User object that will be managed by Flask-Login and work with MongoDB.
    This model should work with Eve framework schema definition. However, 
    this resource type is managed OUTSIDE of eve framework.
    '''
    def __init__(self, username, firstname, middlename, lastname, email, 
        active, anonymous, validated, password_hash=''):   
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
        self.generate_appkey()
    
    
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
        self.appkey = appkey
        return appkey

    
    def update_password(self, newone):
        self.password_hash = generate_password_hash(newone, 
            method=encryption_method)    
        
    def save(self):
        mongo = current_app._get_current_object().data.driver
        obj_str = json.dumps(self, default=lambda o: o.__dict__)
        obj = json.loads(obj_str)
        #print 'new user json is: %s' % obj_str
        mongo.db.users.update({'username':self.username},obj, upsert=True)
        
        
    @staticmethod
    def create(username, password, firstname, middlename, lastname, email):
        mongo = current_app._get_current_object().data.driver
        # To check if username is already existing.
        user = mongo.db.users.find_one({'username': username})
        if user:
            return None # the username is already existing. Throw an exception.
        else:
            # Generate a salted password by using PBKDF2-SHA256
            password_hash = generate_password_hash(password, 
                method=encryption_method)
           
            new_user = User(username=username, password_hash=password_hash,
                firstname=firstname, middlename=middlename, lastname=lastname,
                email=email, active=True, anonymous=False, validated=False)
        
            return new_user       
        
        
    @staticmethod
    def get_with_username(username=''):
        '''
        Return User object that matches a given username by reading a db.
        This method should be called inside of request context in order to get
        current_app object.
        '''
        mongo = current_app._get_current_object().data.driver
        user = mongo.db.users.find_one({'username': username})
        
        if user is None:
            return None
        
        return User(username=user['username'],  firstname=user['firstname'], 
            middlename=user['middlename'], lastname=user['lastname'], 
            email=user['email'], password_hash=user['password_hash'], 
            validated=user['validated'], active=user['active'], 
            anonymous=False)
            
            
    @staticmethod
    def get_with_userid(useroid):
        mongo = current_app._get_current_object().data.driver
        user = mongo.db.users.find_one({'_id': ObjectId(useroid)})
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
        return self.username       
        
'''
class ProjectMember:
    def __init__(self, firstname, middlename, lastname, email):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.email = email
'''         
    
        

class Project:
    '''
    Project object that holds project information.
    This model should work with Eve framework schema definition. However, 
    this resource type is managed OUTSIDE of eve framework.
    '''
    def __init__(self, prj_name, prj_desc, owner, prj_id=None, 
            member_list=[]):
        self.name = prj_name
        self.desc = prj_desc
        self.owner = owner # owner's username
        self.member_list = member_list # object id list of members
        self.prj_id = prj_id
        if prj_id is None:
            self.prj_id = self.create_prj_id()
        
        
    def save(self):
        mongo = current_app._get_current_object().data.driver
        obj_str = json.dumps(self, default=lambda o: o.__dict__)
        obj = json.loads(obj_str)
        #print 'new project json is: %s' % obj_str
        mongo.db.projects.update({'prj_id':self.prj_id}, obj, upsert=True)
        
            
    def create_prj_id(self):
        '''
        System generated project id
        '''
        r_num = 6 # the length of prj_id
        char_range = string.ascii_lowercase + string.digits
        # prj_id is one of IDs that a user need to type into an app.
        mongo = current_app._get_current_object().data.driver
        prj_id = ''.join(random.choice(char_range) for x in range(r_num))
        # Check if prj_id is unique. If not, generate it again.
        while True: 
            prj = mongo.db.projects.find_one({'prj_id': prj_id})
            if prj is None:
                break
            prj_id = ''.join(random.choice(char_range) for x in range(r_num))
        
        return prj_id
        
        
    def add_member(self, firstname, lastname, member_email, middlename=''):
        '''
        Add a member of a project.
        Check if new member's email exists in the member list, and if not, add
        the member to the member list.
        '''
        email_list = {}
        for m in self.member_list:
            email_list[m.email] = True
        
        if meber_email not in email_list.keys():            
            new_member = []
            new_member['firstname'] = firstname
            new_member['middlename'] = middlename
            new_member['lastname'] = lastname
            new_member['email'] = member_email
            self.member_list.append(new_member)
                

    @staticmethod
    def get_projects_for_username(username):
        '''
        Get a list of projects for a user id (user's object id in mongodb)
        '''
        mongo = current_app._get_current_object().data.driver
        projects = mongo.db.projects.find({'owner': username})
        
        prj_list = []
        for row in projects:
            print 'project row', row
            prj = Project(prj_name=row['name'], prj_desc=row['desc'],
                owner=username, prj_id=row['prj_id'])  
            prj_list.append(prj)
        
        return prj_list        
    










        
    
    
    
    