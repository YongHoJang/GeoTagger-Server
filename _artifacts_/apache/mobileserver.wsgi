activate_this = '/home/admin/ENV/4K-mobile-app-server/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/home/admin/ENV/4K-mobile-app-server/prj')

from server import app as application