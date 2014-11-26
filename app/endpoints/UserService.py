from flask_restful import Resource, marshal_with, fields
from flask import request

from app.db import userDao
from app.endpoints import restApi , auth


@restApi.resource("/user/<int:userId>")
class UserResource(Resource):
    get_fields = {
        'id' : fields.Integer(attribute = 'uid'),
        'username' : fields.String,
        'userId' : fields.Integer,
        'spojHandle' : fields.String
    }
    delete_fields = {
        'status' : fields.String,
        'error' : fields.String
    }
    @auth.login_required
    @marshal_with(get_fields)
    def get(self, userId):
        print request.authorization.username
        return userDao.getUserById(userId)
    @marshal_with(delete_fields)
    def delete(self, userId):
        print request.authorization.username
        userDao.removeUserById(userId)
        return {'status' : 'Ok'}
    
    

        


    