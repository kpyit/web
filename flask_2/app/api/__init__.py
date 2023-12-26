from flask import Blueprint
  
api = Blueprint('api', __name__)

#добавил импорт
from . import authentication, posts, users, comments, errors
