import settings
from flask import Blueprint, render_template, abort, request, redirect, flash
from flask import url_for
import requests


proxy_views = Blueprint('proxy', __name__, template_folder='templates')


# Helper functions
# *****
def query_factual(place, country):
    apikey = settings.FACTUAL_APIKEY
    filter_str = '{"$and":[{"country":{"$eq":"%s"}},{"name":{"$search":"%s"}}]}' % (country, place)
    qurl = 'https://api.factual.com/t/world-geographies?filters=%s&KEY=%s' % (filter_str, apikey)
    # send a request
    print 'send a request to factual...'
    print 'query string:' + qurl
    res = requests.get(qurl)
    # TODO: handle errors in response
    
    print res.status_code
    print res.text
    
    # receive & parse a response
    
    # return
    return res.text

    
@proxy_views.route('/q', methods=['GET','POST'])
def query():
    error = None
    # Get a request data
    if request.method == 'GET':
        place = request.args.get('place')
        #province = request.args.get('prov') # province or county
        country = request.args.get('country')
        # TODO: check if country & either (city, province) are filled
        if place is None or country is None:
            return ('You should type country name & place to search', 400,'')
        else:
            qresults = query_factual(place, country)
        return render_template("proxy_success.html", error=error)
    
    else:
        pass
            

        
        
        