from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect
import requests
from flask_cache import Cache

from application import app
from decorators import login_required, admin_required, crossdomain
import configuration

cache = Cache(app)

# @crossdomain(origin='*')
def home(source=None, variant=None, edition=None):
    api_url = configuration.lookup('CONTENT_API_URL')
    payload = {
        'api-key':              configuration.lookup('CONTENT_API_KEY'),
        'page-size':            10,
        'show-editors-picks':   'true',
        'show-elements':        'image',
        'show-fields':          'all',
        'edition':              edition
    }
    response = requests.get(api_url, params=payload)
    data = response.json()['response']['editorsPicks']
    return render_template('index.html', content=data)


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''
