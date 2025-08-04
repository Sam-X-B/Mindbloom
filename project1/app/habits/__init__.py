from flask import Blueprint

bp = Blueprint('habits', __name__)

from app.habits import routes  # This import MUST come after bp creation
