from flask import Blueprint

#создание чертежа
parser = Blueprint('parser', __name__)

from . import views
