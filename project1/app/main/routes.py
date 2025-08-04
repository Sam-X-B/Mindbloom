from flask import Blueprint, render_template, redirect, url_for,request,flash,Flask
from flask_login import current_user,login_required
from flask_wtf.csrf import CSRFProtect
from flask import Blueprint
from app.main import bp
from .. import db

app = Flask(__name__)
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')
@main_bp.route('/about')
def about():
    return render_template('about.html', title='About MindBloom')
@main_bp.route('/toggle-dark-mode', methods=['POST'])
def toggle_dark_mode():
    session['dark_mode'] = not session.get('dark_mode', False)
    return jsonify({'dark_mode': session['dark_mode']})
@main_bp.route('/help')
def help():
    return render_template('help.html')
@main_bp.route('/feedback', methods=['POST'])
def feedback():
    try:
        feedback = Feedback(
            user_id=current_user.id if current_user.is_authenticated else None,
            message=request.form.get('message'),
            category=request.form.get('category', 'general')
        )
        db.session.add(feedback)
        db.session.commit()
        flash('Thank you for your feedback!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Failed to submit feedback', 'error')
        app.logger.error(f"Feedback error: {str(e)}")

    return redirect(request.referrer or url_for('main.help'))
@main_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        return handle_settings_post()
    return handle_settings_get()

def handle_settings_post():
    try:
        settings_type = request.form.get('settings_type')

        if not settings_type:
            flash('Invalid settings request', 'error')
            return redirect_back()

        handlers = {
            'account': handle_account_settings,
            'notifications': handle_notification_settings,
            'privacy': handle_privacy_settings,
            'theme': handle_theme_settings
        }

        if settings_type in handlers:
            handlers[settings_type]()
            flash(f'{settings_type.capitalize()} settings updated!', 'success')
        else:
            flash('Invalid settings type', 'error')

        return redirect_back()

    except Exception as e:
        db.session.rollback()
        flash(f'Error saving settings: {str(e)}', 'error')
        return redirect_back()

def handle_account_settings():
    current_user.display_name = request.form.get('display_name', current_user.display_name)
    current_user.email = request.form.get('email', current_user.email)
    current_user.email_visible = 'email_visible' in request.form
    db.session.commit()

def handle_notification_settings():
    current_user.email_notifications = 'email_notifications' in request.form
    current_user.push_notifications = 'push_notifications' in request.form
    current_user.reminder_emails = 'reminder_emails' in request.form
    current_user.notification_frequency = request.form.get(
        'notification_frequency',
        current_user.notification_frequency or 'instant'
    )
    db.session.commit()

def handle_privacy_settings():
    current_user.profile_visibility = request.form.get(
        'profile_visibility',
        current_user.profile_visibility or 'private'
    )
    current_user.analytics_tracking = 'analytics_tracking' in request.form
    current_user.personalized_ads = 'personalized_ads' in request.form
    db.session.commit()

def handle_theme_settings():
    current_user.theme_preference = request.form.get(
        'theme_preference',
        current_user.theme_preference or 'system'
    )
    current_user.accent_color = request.form.get(
        'accent_color',
        current_user.accent_color or 'primary'
    )
    # Update session for immediate theme change
    if current_user.theme_preference == 'dark':
        session['dark_mode'] = True
    elif current_user.theme_preference == 'light':
        session['dark_mode'] = False
    db.session.commit()

def handle_settings_get():
    return render_template('layout.html',
                         current_user=current_user,
                         nav_items=get_nav_items(),
                         social_links=get_social_links())

def redirect_back():
    return redirect(request.referrer or url_for('main.home'))
