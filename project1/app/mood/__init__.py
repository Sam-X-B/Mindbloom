from flask import Blueprint

bp = Blueprint('mood', __name__)

from app.mood import routes  # This import MUST come after bp creation
