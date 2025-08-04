from flask import Blueprint

bp = Blueprint('affirmations', __name__)

from app.affirmations import routes  # This import MUST come after bp creation
