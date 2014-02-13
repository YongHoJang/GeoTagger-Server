import os
from eve import Eve
from user.views import user_views
from flask.ext.login import LoginManager
from user.models import User
from user.views import login


# Setup app!
# ---
SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
app = Eve(settings=SETTINGS_PATH)
# Blueprint Configuration
app.register_blueprint(user_views, url_prefix='/user')
# TODO: Need to configure it for individual application
app.secret_key = 'B1Xp83k/4qY1S~GIH!jnM]KES/,?CT'
# Support multiprocesses.
app.processes = 4

# Flask-Login Configuration
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)
login_manager.login_view = '/user/login'


# Required method to connect Flask-Login with custom User class
@login_manager.user_loader
def load_user(username):
    print 'load_user- userid', username
    return User.get_with_username(username)


if __name__ == '__main__':
    app.debug = True
    # set processes param for mulpiple concurrent users.
    app.run(host='0.0.0.0', port=5000)



