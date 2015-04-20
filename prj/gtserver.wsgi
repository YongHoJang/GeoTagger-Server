activate_this = '/home/mserver/ENV/4K-mobile-app-server/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# put server.py into python path.
import sys
sys.path.insert(0, '/home/mserver/ENV/4K-mobile-app-server/prj')

from server import app as application