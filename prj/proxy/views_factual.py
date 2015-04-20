import settings
from flask import Blueprint, render_template, abort, request, Response, redirect, flash
from flask import url_for
from flask import current_app as app
import requests
import json



proxy_views = Blueprint('proxy', __name__, template_folder='templates')


# Helper functions
# *****
def find_countrycode(cntrystr):
    # Find a proper country code for user's free text input
    # Return None if user's input is not found
    result = cntrystr
    return result


def query_factual(place, country):
    apikey = settings.FACTUAL_APIKEY
    filter_str = '{"$and":[{"country":{"$eq":"%s"}},{"name":{"$search":"%s"}}]}' % (country, place)
    qurl = 'https://api.factual.com/t/world-geographies?filters=%s&KEY=%s' % (filter_str, apikey)
    # send a request
    #print 'send a request to factual...'
    #print 'query string:' + qurl
    app.logger.info('query string to factual: %s' % qurl)
    res = requests.get(qurl)
    # TODO: handle errors in response
    response = Response(response=res.text, status = res.status_code, 
        mimetype="application/json")
    return  response

    
@proxy_views.route('/q', methods=['GET'])
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
            cntrycode = find_countrycode(country)
            if cntrycode is None:
                return ('You should type a valid country name ', 400,'')
            response = query_factual(place, cntrycode)
        return response
        #return render_template("proxy_success.html", error=error)
    else:
        pass
            

        
        
        