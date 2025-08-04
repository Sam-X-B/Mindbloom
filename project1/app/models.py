from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    # Core Authentication Fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Relationships
    journal_entries = db.relationship('JournalEntry', backref='author', lazy='dynamic', cascade='all, delete-orphan')
    mood_entries = db.relationship('MoodEntry', backref='author', lazy='dynamic')
    habits = db.relationship('Habit', backref='author', lazy='dynamic')
    goals = db.relationship('Goal', backref='author', lazy='dynamic')
    affirmations = db.relationship('Affirmation', backref='owner', lazy='dynamic', cascade='all, delete-orphan')
    habit_logs = db.relationship('HabitLog', backref='user', lazy='dynamic')

    # Settings Fields
    display_name = db.Column(db.String(50))
    email_visible = db.Column(db.Boolean, default=False)
    email_notifications = db.Column(db.Boolean, default=True)
    push_notifications = db.Column(db.Boolean, default=True)
    reminder_emails = db.Column(db.Boolean, default=True)
    notification_frequency = db.Column(db.String(20), default='instant')
    profile_visibility = db.Column(db.String(20), default='private')
    analytics_tracking = db.Column(db.Boolean, default=True)
    personalized_ads = db.Column(db.Boolean, default=False)
    theme_preference = db.Column(db.String(20), default='system')
    accent_color = db.Column(db.String(20), default='primary')

    # Methods
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(150))
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(100))
    mood = db.Column(db.String(10))
    date = db.Column(db.DateTime, default=datetime.utcnow)

class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mood = db.Column(db.String(10), nullable=False)
    notes = db.Column(db.Text)
    tags = db.Column(db.String(100))
    reflection = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    frequency = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    logs = db.relationship('HabitLog', backref='habit', lazy='dynamic')

class HabitLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    target_date = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='open')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Affirmation(db.Model):
    __tablename__ = 'affirmations'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
class Feedback(db.Model):
    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    message = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), default='general')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='open')
    user = db.relationship('User', backref='feedback_submissions')
