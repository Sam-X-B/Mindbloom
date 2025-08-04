from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import db
from ..models import Habit, HabitLog
from datetime import datetime, timedelta
from flask_wtf.csrf import CSRFProtect

habits_bp = Blueprint('habits', __name__)

@habits_bp.route('/habits/mark_done/<int:habit_id>', methods=['POST'])
@login_required
def mark_done(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    if habit.user_id != current_user.id:
        abort(403)
    log = HabitLog(user_id=current_user.id, habit_id=habit_id)
    db.session.add(log)
    db.session.commit()
    flash('Habit logged!', 'success')
    return redirect(url_for('habits.habits'))

@habits_bp.route('/habits/edit', methods=['POST'])
@login_required
def edit_habit():
    habit_id = request.form.get('habit_id')
    habit = Habit.query.get_or_404(habit_id)

    if habit.user_id != current_user.id:
        abort(403)

    habit.name = request.form['name']
    habit.category = request.form.get('category', '')
    habit.frequency = request.form.get('frequency', habit.frequency)
    db.session.commit()

    flash('Habit updated!', 'success')
    return redirect(url_for('habits.habits'))

@habits_bp.route('/habits', methods=['GET', 'POST'])
@login_required
def habits():
    if request.method == 'POST' and 'habit_id' not in request.form:
        name = request.form['name']
        category = request.form.get('category')
        days = request.form.getlist('days')
        freq_csv = ','.join(days)

        habit = Habit(
            user_id=current_user.id,
            name=name,
            category=category,
            frequency=freq_csv
        )
        db.session.add(habit)
        db.session.commit()
        flash(f'Habit "{name}" added!', 'success')
        return redirect(url_for('habits.habits'))

    raw_habits = Habit.query.filter_by(user_id=current_user.id).all()

    habit_list = []
    for h in raw_habits:
        total_logs = HabitLog.query.filter_by(
            user_id=current_user.id,
            habit_id=h.id
        ).count()

        logs = HabitLog.query.filter_by(habit_id=h.id).order_by(HabitLog.completed_at.desc()).all()
        streak = 0
        current_date = datetime.utcnow().date()
        for log in logs:
            if log.completed_at.date() == current_date - timedelta(days=streak):
                streak += 1
            else:
                break

        days_count = max(len(h.frequency.split(',')), 1)
        completion = min(100, int((total_logs / days_count) * 100))

        habit_list.append({
            'id': h.id,
            'name': h.name,
            'category': h.category,
            'frequency': h.frequency,
            'streak': streak,
            'completion': completion
        })

    now = datetime.utcnow()
    one_week_ago = now - timedelta(days=7)
    two_weeks_ago = now - timedelta(days=14)

    completed_week = HabitLog.query.filter(
        HabitLog.user_id == current_user.id,
        HabitLog.completed_at >= one_week_ago
    ).count()

    last_week_completed = HabitLog.query.filter(
        HabitLog.user_id == current_user.id,
        HabitLog.completed_at >= two_weeks_ago,
        HabitLog.completed_at < one_week_ago
    ).count()

    delta_completed = completed_week - last_week_completed
    avg_this_week = round(completed_week / 7, 1)
    avg_last_week = round(last_week_completed / 7, 1)
    longest_streak = max((h['streak'] for h in habit_list), default=0)

    stats = {
        'completed': completed_week,
        'average_daily': avg_this_week,
        'longest_streak': longest_streak,
        'trend': {
            'completed': f"{delta_completed:+}",
            'average_daily': f"{(avg_this_week - avg_last_week):+.1f}"
        }
    }

    suggestions = [
        'Drink a glass of water first thing',
        'Read for 10 minutes',
        'Write down three things you are grateful for',
        'Take a 5-minute stretch break'
    ]

    return render_template(
        'habits.html',
        habits=habit_list,
        stats=stats,
        suggestions=suggestions
    )
