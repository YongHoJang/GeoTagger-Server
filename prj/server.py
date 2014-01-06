import os
from eve import Eve
from account.views import account_views
from flask.ext.login import LoginManager


# Setup app!
# ---
SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
app = Eve(settings=SETTINGS_PATH)

# Blueprint Configuration
app.register_blueprint(account_views, url_prefix='/account')

# Flask-Login Configuration
login_manager = LoginManager()
login_manager.init_app(app)


if __name__ == '__main__':
    app.debug = True
    app.run()



