from marshmallow import fields, Schema
import datetime
from . import db

class UserModel(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  lastname = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  phone = db.Column(db.Integer, nullable=True)
  typeId = db.Column(db.String(128), nullable=False)
  birthday = db.Column(db.DateTime)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  def __init__(self, data):
    self.name = data.get('name')
    self.email = data.get('email')
    self.lastname = data.get('lastname')
    self.phone = data.get('phone')
    self.typeId = data.get('typeId')
    self.birthday = data.get('birthday')
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  @staticmethod
  def get_all_users():
    return UserModel.query.all()

  @staticmethod
  def get_one_user(id):
    return UserModel.query.get(id)

class UserSchema(Schema):

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    lastname = fields.Str(required=True)
    phone = fields.Str(required=True)
    typeId = fields.Str(required=True)
    birthday = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
