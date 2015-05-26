from flask import render_template, Blueprint, render_template, abort, request
from flask import url_for, redirect
from flask.ext.login import login_user, login_required
from flask.ext.login import logout_user, current_user
from gt_app.account.models import User, Project
from models import SurveyForm

# Define the blueprint
dstore_views = Blueprint('dstore', __name__, template_folder='templates',
    static_folder='static')


@dstore_views.route('/projdatamap/<prj_id>', methods=['GET','POST'])
@login_required
def projdata_map(prj_id):
    
    # First, get project info
    prj = Project.get_project_for_projectid(prj_id)
    # Validate a request
    if prj is None or (prj.owner != current_user.username):
        return render_template('404.html')    
    
    # Fetch project data from db, first 1000 data.
    
    
    return render_template('projdata_map.html', prj=prj)
    

@dstore_views.route('/form/<form_id>', methods=['GET','POST'])
@login_required
def dataform_submit(form_id):

    # First, get survey form info
    '''
    prj = Project.get_project_for_projectid(prj_id)
    # Validate a request
    if prj is None or (prj.owner != current_user.username):
        return render_template('404.html')
    '''
        
    if (request.method == "GET"):
        # Get data form
        survey = SurveyForm ('','','')
        form_html = survey.to_html('/form/'+ form_id)
        return render_template('dataform.html', form_html=form_html)
        
    elif (request.method == "POST"):
        return render_template('dataform_done.html')
        
    else:
        return render_template('dataform_done.html')



    
    