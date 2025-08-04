from urllib.parse import urlparse
from flask import Blueprint, request, abort, current_app
from flask_login import current_user

# Create blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.before_request
def auth_protection():
    """Protect sensitive auth endpoints without direct app import"""
    if request.method == 'POST' and request.endpoint in ['auth.change_password', 'auth.edit_profile']:
        if not current_user.is_authenticated:
            abort(403)
        if request.referrer and urlparse(request.referrer).netloc != request_app().host:
            abort(403)

def request_app():
    """Safe access to current app instance"""
    return current_app._get_current_object()

def init_auth(app):
    """Initialize auth components with app context"""
    from . import routes  # Import routes AFTER app is available

    # Register security headers
    @app.after_request
    def apply_security_headers(response):
        response.headers.update({
            'Referrer-Policy': 'strict-origin-when-cross-origin',
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'SAMEORIGIN'
        })
        return response

    app.register_blueprint(auth_bp)
    return auth_bp
