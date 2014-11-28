from flask_restful import Resource, marshal_with, fields, reqparse
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
    @marshal_with(get_fields)
    def get(self, userId):
        print request.authorization.username
        return userDao.getUserById(userId)
    @marshal_with(delete_fields)
    def delete(self, userId):
        print request.authorization.username
        userDao.removeUserById(userId)
        return {'status' : 'Ok'}
    
    
@restApi.resource("/user/getToken")
class AuthenticationResource(Resource):
    post_field = {
        'status' : fields.String,
        'error' : fields.String,
        'token' : fields.String,
        'username' : fields.String(default=''),
        'name' : fields.String(default=''),
        'isOnline': fields.Boolean(default = False),
        'id': fields.Integer(default = None)
    }
    @marshal_with(post_field)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='Username is required')
        parser.add_argument('password', type=str, help='Password is required')
        credentials = parser.parse_args()
        usr = userDao.getUserByUsername(credentials.username)
        if usr == None:
            return {'status' : 'UNotFound' , 'error': 'User does not exist'}
        if usr.password != credentials.password :
            return {'status' : 'IncPass' , 'error': 'Wrong Password'}
        return {'status': 'Ok' , 
                'token': '=1=%s=1=%s=1=' % (credentials.username , credentials.password),
                'username': credentials.username,
                'name' : 'Test User',
                'isOnline': True,
                'id': usr.id}
    @auth.login_required
    def get(self):
        return {'response' : "secret"}


    