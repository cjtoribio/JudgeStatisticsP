from flask import Flask
from flask_restful import Resource, reqparse
import flask_restful
import json
import math

from app.db import subsDao
from app.model.Submission import Submission
from app.util import DateUtils
from app.util.DateUtils import DateFormat


port = Flask(__name__, static_folder='../../public', static_url_path='')

restApi = flask_restful.Api(port)

def restResourceDecorator(*urls, **kwargs):
    def decorator(clazz):
        print "Registered urls:" , urls
        restApi.add_resource(clazz, *urls , **kwargs)
        return clazz
    return decorator
restApi.resource = restResourceDecorator


import SpojService
import UserService
    
    

if __name__ == "__main__":
    port.run()