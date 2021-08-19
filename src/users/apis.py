from flask_restx import Resource, Namespace


api = Namespace('users', description='Users API')


@api.route('/')
class Users_API(Resource):
    """Users API

    Args:
        Resource ([type]): [description]
    """    
    def get(self):
        return {'user list': True}