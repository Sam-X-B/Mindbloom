from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .. import db
from ..models import JournalEntry
from flask_wtf.csrf import CSRFProtect
from flask import Blueprint
from app.journal import bp

journal_bp = Blueprint('journal', __name__)

@journal_bp.route('/journal', methods=['GET', 'POST'])
@login_required
def journal():
    if request.method == 'POST':
        entry = JournalEntry(
            user_id=current_user.id,
            title=request.form.get('title'),
            content=request.form['content'],
            tags=request.form.get('tags'),
            mood=request.form.get('mood')
        )
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('journal.journal'))

    entries = JournalEntry.query \
        .filter_by(user_id=current_user.id) \
        .order_by(JournalEntry.date.desc()) \
        .all()

    return render_template('journal.html', entries=entries)

