from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import db
from ..models import Affirmation
import random
from flask_wtf.csrf import CSRFProtect
from flask import Blueprint
from app.affirmations import bp

affirmations_bp = Blueprint('affirmations', __name__)

@affirmations_bp.route('/affirmations', methods=['GET', 'POST'])
@login_required
def affirmations():
    if request.method == 'POST':
        text = request.form.get('new_affirmation', '').strip()
        if text:
            if len(text) < 5:  # Moved validation before DB operations
                flash('Affirmation too short', 'warning')
                return redirect(url_for('affirmations'))

            af = Affirmation(text=text, owner=current_user)
            db.session.add(af)
            db.session.commit()
            flash('Affirmation added!', 'success')
        else:
            flash('Type something before submitting.', 'warning')
            return redirect(url_for('affirmations'))

    choices = current_user.affirmations.order_by(
        Affirmation.created.desc()
    ).all()

    featured = random.choice(choices) if choices else None

    return render_template(
        'affirmations.html',
        featured_affirmation=featured.text if featured else None,
        affirmations=[a.text for a in choices]
    )
