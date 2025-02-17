#!/usr/bin/python3
'''module api/v1/views/index.py:
create a route `/status` on the object app_views
returns a jsonified response: 'status': 'OK'
'''
from flask import jsonify

from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def api_status():
    '''route:GET
    returns a JSON response for RESTful API health
    '''
    return jsonify(
        {
            'status': 'OK'
        }
    )


@app_views.route('/stats', methods=['GET'])
def get_stats():
    '''get stats
    retrieves the number of each objects by type
    '''
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)