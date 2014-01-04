import os
from eve import Eve
from website.view import website


# Setup app!
# ---
SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
#app = Eve(auth=HMACAuth, settings=SETTINGS_PATH)
app = Eve(settings=SETTINGS_PATH)
app.register_blueprint(website, url_prefix='/website')


if __name__ == '__main__':
    app.debug = True
    app.run()



