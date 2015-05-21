import app.gts_settings
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
    # TODO: repackage the response to contain only necessary info. 
    res_json = json.loads(res.text)
    res_status = res_json['status']
    if res_status == 'ok':
        resultdict = {}
        resultdict['num_data'] = res_json['response']['included_rows']
        resultdict['data'] = []
        for data in res_json['response']['data']:
            entry = {}
            entry['contextname'] = data['contextname']
            entry['fact_id'] = data['factual_id'];
            entry['latitude'] = data['latitude'];
            entry['longitude'] = data['longitude'];
            resultdict['data'].append(entry)
        res_text = json.dumps(resultdict)
    else:
        # Error happened in factual query. 
        # TODO: handle it properly
        res_text = json.dumps('{}')
    # TODO: handle errors in response
    #print "Factual API response inside of query_factual:", res.text
    response = Response(response=res_text, status = res.status_code, 
        mimetype="application/json")
    return  response

    
@proxy_views.route('/q', methods=['GET', 'POST'])
def query():
    # TODO: Validate user's query privilege using clients' app key and account
    # -----
    
    error = None
    # Get a request data
    if request.method == 'GET':
        place = request.args.get('place')
        country = request.args.get('country')
    elif request.method == 'POST':
        place = request.form.get('place')
        country = request.form.get('country')
    else:
        pass
            
    # TODO: check if country & either (city, province) are filled
    if place is None or country is None:
        return ('You should type country name & place to search', 400,'')
    else:
        cntrycode = find_countrycode(country)
        if cntrycode is None:
            return ('You should type a valid country name ', 400,'')
        response = query_factual(place, cntrycode)
        return response
            

        
        
        