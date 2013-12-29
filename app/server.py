import os
from eve import Eve
from eve.auth import BasicAuth, HMACAuth
from werkzeug.security import check_password_hash
from mapviewer.view import mapviewer
from website.view import website
from hashlib import sha1
import hmac


# Supported Authentication
# ---
class HMACAuth(HMACAuth):
    def check_auth(self, username, hmac_hash, headers, data, allowed_roles,
            resource, method):
        # use Eve's own db driver; no additional connections/resources are
        # used
        accounts = app.data.driver.db['accounts']
        user = accounts.find_one({'username': username})
        if user:
            secret_key = user['secret_key']
        # in this implementation we only hash request data, ignoring the
        # headers.
        return ( user and 
            hmac.new(str(secret_key), str(data), sha1).hexdigest() == hmac_hash) 



class Sha1Auth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        # If you saved a hashed password in db.
        return account and assword == account['password'] 
        # If you saved a clear text password
        #return account and check_password_hash(account['password'], password) 



# Setup app!
# ---
SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
app = Eve(auth=HMACAuth, settings=SETTINGS_PATH)
app.register_blueprint(mapviewer, url_prefix='/mapviewer')
app.register_blueprint(website, url_prefix='/website')


if __name__ == '__main__':
    app.debug = True
    app.run()



