from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes  # This import MUST come after bp creation
