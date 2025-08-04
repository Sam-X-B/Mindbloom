from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .. import db, login_manager
from ..models import User
from flask_wtf.csrf import CSRFProtect

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('journal.journal'))

    if request.method == 'POST':
        from flask_wtf.csrf import validate_csrf
        from wtforms import ValidationError

        try:
            validate_csrf(request.form.get('csrf_token'))
        except ValidationError:
            abort(400)
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']

        if password != confirm:
            flash("Passwords do not match", "danger")
            return render_template('register.html')
        elif User.query.filter((User.username == username) | (User.email == email)).first():
            flash("Username or email already taken.", "warning")
        else:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash("Account created! You can now log in.", "success")
            return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('journal'))

    if request.method == 'POST':
        from flask_wtf.csrf import validate_csrf
        from wtforms import ValidationError

        try:
            validate_csrf(request.form.get('csrf_token'))
        except ValidationError:
            abort(400)
        identifier = request.form['identifier']
        password = request.form['password']
        user = User.query.filter((User.username == identifier) | (User.email == identifier)).first()

        if user and user.check_password(password):
            login_user(user)
            flash(f"Welcome back, {user.username}!", "info")
            return redirect(url_for('journal.journal'))
        else:
            flash("Invalid credentials.", "danger")

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.", "info")
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@auth_bp.route('/edit-profile', methods=['POST'])
@login_required
def edit_profile():
    new_name = request.form.get('fullname')
    new_email = request.form.get('email')

    # Basic validation
    if not new_name or not new_email:
        flash('All fields are required', 'error')
        return redirect(request.referrer)

    current_user.fullname = new_name
    current_user.email = new_email
    db.session.commit()

    flash('Profile updated!', 'success')
    return redirect(request.referrer or url_for('main.home'))

@auth_bp.route('/change-password', methods=['POST'])
@login_required
def change_password():
    current_pw = request.form.get('current_password')
    new_pw = request.form.get('new_password')

    if not current_user.check_password(current_pw):
        flash('Current password is incorrect', 'error')
        return redirect(request.referrer)

    current_user.set_password(new_pw)
    db.session.commit()

    flash('Password changed!', 'success')
    return redirect(url_for('auth.login'))  
