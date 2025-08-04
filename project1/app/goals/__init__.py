from flask import Blueprint

bp = Blueprint('goals', __name__)

from app.goals import routes  # This import MUST come after bp creation
