from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import db
from ..models import Goal
from datetime import datetime
from flask_wtf.csrf import CSRFProtect

STATUS_COLORS = {
    'completed': '#28a745',
    'in_progress': '#ffc107',
    'open': '#dee2e6'
}

goals_bp = Blueprint('goals', __name__)

@goals_bp.route('/goals', methods=['GET', 'POST'])
@login_required
def goals():
    today = datetime.utcnow().date()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description')
        target_date_str = request.form.get('target_date')
        status = request.form.get('status', 'open')
        target_date = None

        try:
            if target_date_str:
                target_date = datetime.strptime(target_date_str, '%Y-%m-%d').date()
                if target_date < today:
                    flash("Target date cannot be in the past", "warning")
                    return redirect(url_for('goals.goals'))

        except ValueError:
            flash('Invalid date format', 'danger')
            return redirect(url_for('goals.goals'))

        goal = Goal(
            user_id=current_user.id,
            title=title,
            description=description,
            target_date=target_date,
            status=status,
            created_at=datetime.utcnow()
        )
        db.session.add(goal)
        db.session.commit()
        flash(f'Goal "{title}" added successfully!', 'success')
        return redirect(url_for('goals.goals'))

    raw_goals = Goal.query.filter_by(user_id=current_user.id).order_by(Goal.created_at.desc()).all()

    goals = []
    for g in raw_goals:
        progress = {
            'completed': 100,
            'in_progress': Goal.query.filter_by(user_id=current_user.id, status='in_progress').count() * 20,
            'open': Goal.query.filter_by(user_id=current_user.id, status='open').count() * 10
        }.get(g.status, 0)

        goals.append({
            'id': g.id,
            'title': g.title,
            'description': g.description,
            'target_date': g.target_date,
            'status': g.status,
            'progress_percent': progress,
           'is_past_due': g.target_date.date() < today if g.target_date else False
                 })

    stats = {
        'total_goals': len(goals),
        'completed': sum(1 for g in goals if g['status'] == 'completed'),
        'in_progress': sum(1 for g in goals if g['status'] == 'in_progress'),
        'open': sum(1 for g in goals if g['status'] == 'open'),
        'past_due': sum(1 for g in goals if g.get('is_past_due') and g['status'] != 'completed')
    }

    suggestions = [
        'Create a savings plan',
        'Run a 10K race',
        'Start journaling daily',
        'Launch a side project'
    ]

    return render_template(
        'goals.html',
        goals=goals,
        stats=stats,
        suggestions=suggestions,
        colors=[STATUS_COLORS.get(g['status'], '#999999') for g in goals],
        today=today
    )
