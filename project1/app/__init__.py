from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from config import Config

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    login_manager.login_view = 'auth.login'

    # Import models after db initialization
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    register_blueprints(app)

    # Register context processor
    register_context_processors(app)

    return app

def register_blueprints(app):
    """Register all blueprints with consistent naming"""
    from app.main.routes import main_bp
    from app.auth.routes import auth_bp
    from app.journal.routes import journal_bp
    from app.mood.routes import mood_bp
    from app.habits.routes import habits_bp
    from app.goals.routes import goals_bp
    from app.affirmations.routes import affirmations_bp
    from app.main.routes import main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(journal_bp)
    app.register_blueprint(mood_bp)
    app.register_blueprint(habits_bp)
    app.register_blueprint(goals_bp)
    app.register_blueprint(affirmations_bp)

def register_context_processors(app):
    """Register context processors"""
    @app.context_processor
    def inject_nav_data():
        from flask import url_for
        return {
            'nav_items': [
                ('Home', url_for('main.home'), 'home'),
                ('Journal', url_for('journal.journal'), 'book'),
                ('Mood', url_for('mood.mood'), 'smile'),
                ('Habits', url_for('habits.habits'), 'repeat'),
                ('Goals', url_for('goals.goals'), 'flag'),
                ('Affirmations', url_for('affirmations.affirmations'), 'heart'),
                ('About', url_for('main.about'), 'info-circle'),
            ],
            'social_links': [
                ('Twitter', '#', 'twitter'),
                ('Instagram', '#', 'instagram'),
                ('Facebook', '#', 'facebook')
            ]
        }
