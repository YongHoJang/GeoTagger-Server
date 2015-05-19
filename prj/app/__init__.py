import os
from eve import Eve
from flask.ext.login import LoginManager
from schemas import domain

# for using gunicorn
from werkzeug.contrib.fixers import ProxyFix


# Setup app!
# ---
# OLD WAY
#SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
#print "SETTINGS_PATH: ", SETTINGS_PATH
#app = Eve(settings=SETTINGS_PATH)

EVE_SETTINGS = {
    'DOMAIN': domain,
}
# NEW ONE
app = Eve(settings=EVE_SETTINGS)
app.config.from_object('settings')



# Blueprint Configuration
from proxy.views_factual import proxy_views
from account.views import account_views, login
from account.models import User

app.register_blueprint(account_views, url_prefix='/account')
app.register_blueprint(proxy_views, url_prefix='/proxy')


# Flask-Login Configuration
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)
login_manager.login_view = '/user/login'

app.wsgi_app = ProxyFix(app.wsgi_app)

# Required method to connect Flask-Login with custom User class
@login_manager.user_loader
def load_user(username):
    print 'load_user- userid', username
    return User.get_with_username(username)
