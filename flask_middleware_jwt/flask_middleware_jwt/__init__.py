import requests
from functools import wraps
from flask import request, jsonify, current_app
import os
import jwt
import json
import logging

logger = logging.getLogger(__name__)



CONFIG_DEFAULTS = {
    'MIDDLEWARE_URL_IDENTITY': '0.0.0.0:5000',
    'MIDDLEWARE_VERIFY_ENDPOINT': '/token/verify',
    'MIDDLEWARE_BEARER': True,
    'MIDDLEWARE_VERIFY_HTTP_VERB': 'GET',
    'JWT_SECRET': 'YOUR_SECRET_KEY'
}

def middleware_jwt_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        
        validate_key() 

        if current_app.config.get('MIDDLEWARE_BEARER'):
            validate_bearer()            

        response = middleware_request(request.headers["Authorization"])

        response_content = json.loads(response.content)

        if response.status_code != 200:
            return jsonify(response_content), response.status_code
        return f(*args, **kwargs)
    return decorator

def validate_key():
    if "Authorization" not in list(request.headers.keys()):
        return jsonify({'message': 'Authorization not found'}), 404

def validate_bearer():
    if 'Bearer ' not in request.headers["Authorization"]:
        return jsonify({'message': 'Authorization no serialized'}), 404


def get_jwt():
    header = request.headers["Authorization"]
    header = header.replace('Bearer ','')
    return header

def get_jwt_identity():
    return get_raw_jwt()['identity']

def get_raw_jwt():
    header = get_jwt()
    return jwt.decode(header, current_app.config.get('JWT_SECRET'), algorithms=['HS256'])

def middleware_request(token):
    try:
        if current_app.config.get('MIDDLEWARE_VERIFY_HTTP_VERB') == 'GET':
            return middleware_get_request(token)
            
        return middleware_post_request(token)
    except Exception as e:
        logger.error(e)
        return jsonify({'message': 'API OFFLINE'}), 500

def middleware_get_request(token):
    return requests.get('{}{}'.format(current_app.config.get('MIDDLEWARE_URL_IDENTITY')
                                         ,current_app.config.get('MIDDLEWARE_VERIFY_ENDPOINT'))
                           ,headers={"Authorization": token})

def middleware_post_request(token):
    return requests.post('{}{}'.format(current_app.config.get('MIDDLEWARE_URL_IDENTITY')
                                         ,current_app.config.get('MIDDLEWARE_VERIFY_ENDPOINT'))
                           ,headers={"Authorization": token})

class Middleware(object):
    def __init__(self, app):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        for k, v in CONFIG_DEFAULTS.items():
            if k not in app.config.keys():
                app.config.setdefault(k, v)
