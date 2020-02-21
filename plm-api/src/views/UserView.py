from flask import request, json, Response, Blueprint
from ..models.UserModel import UserModel, UserSchema

user_api = Blueprint('users', __name__)
user_schema = UserSchema()

@user_api.route('/', methods=['POST'])
def create():
  req_data = request.get_json()
  data, error = user_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  user_in_db = UserModel.get_user_by_email(data.get('email'))
  if user_in_db:
    message = {'error': 'El usuario ya existe en la DB'}
    return custom_response(message, 400)
  
  user = UserModel(data)
  user.save()

  ser_data = user_schema.dump(user).data

  return custom_response(201)
  

def custom_response(res, status_code):
    return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
)