from flask import render_template, Blueprint
from flask.ext.login import login_user, login_required
from flask.ext.login import logout_user, current_user
from gt_app.account.models import User, Project

# Define the blueprint
dstore_views = Blueprint('dstore', __name__, template_folder='templates',
    static_folder='static')


@dstore_views.route('/projdatamap/<prj_id>', methods=['GET','POST'])
def projdata_map(prj_id):
    
    # First, get project info
    prj = Project.get_project_for_projectid(prj_id)
    # Validate a request
    if prj is None or (prj.owner != current_user.username):
        return render_template('404.html')    
    
    # Fetch project data from db, first 1000 data.
    
    
    return render_template('projdata_map.html', prj=prj)
    




    
    