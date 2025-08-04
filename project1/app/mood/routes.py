from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .. import db
from ..models import MoodEntry
from datetime import datetime, timedelta
import random


mood_bp = Blueprint('mood', __name__)

# Sample affirmations and questions
AFFIRMATIONS = [
    "I am in control of my emotions",
    "My feelings are valid and important",
    "I allow myself to feel without judgment",
    "Every day brings new opportunities for joy",
    "I am resilient and can handle whatever comes my way"
]

DAILY_QUESTIONS = [
    "What's one small thing that brought you joy today?",
    "How could you show yourself kindness right now?",
    "What emotion do you need to acknowledge today?",
    "What's something you're grateful for in this moment?"
]

@mood_bp.route('/mood', methods=['GET', 'POST'])
@login_required
def mood():
    if request.method == 'POST':
        # Process mood form submission
        mood = request.form.get('mood')
        notes = request.form.get('notes', '').strip()
        tags = request.form.getlist('tags')
        reflection = request.form.get('reflection', '').strip()

        # Create new mood entry
        entry = MoodEntry(
            user_id=current_user.id,
            mood=mood,
            notes=notes,
            tags=','.join(tags) if tags else None,
            reflection=reflection if reflection else None
        )

        db.session.add(entry)
        db.session.commit()

        flash('Your mood has been recorded!', 'success')
        return redirect(url_for('mood.mood'))

    # Calculate insights
    entries = MoodEntry.query.filter_by(user_id=current_user.id).all()

    insights = {
        'average': calculate_average_mood(entries),
        'common': most_common_mood(entries),
        'streak': current_streak(entries),
        'reflections': sum(1 for e in entries if e.reflection)
    } if entries else {
        'average': 0,
        'common': 'No data',
        'streak': 0,
        'reflections': 0
    }

    return render_template(
        'mood.html',
        affirmation=random.choice(AFFIRMATIONS) if entries else None,
        insights=insights,
        daily_question=random.choice(DAILY_QUESTIONS)
    )

def calculate_average_mood(entries):
    if not entries:
        return 0

    mood_values = {
        '😊': 5,
        '😐': 3,
        '😢': 1,
        '😡': 2,
        '😴': 2
    }

    total = sum(mood_values.get(e.mood, 0) for e in entries)
    return round(total / len(entries), 1)

def most_common_mood(entries):
    if not entries:
        return "No data"

    mood_counts = {}
    for e in entries:
        mood_counts[e.mood] = mood_counts.get(e.mood, 0) + 1

    return max(mood_counts.items(), key=lambda x: x[1])[0]

def current_streak(entries):
    if not entries:
        return 0

    # Sort entries by date (newest first)
    sorted_entries = sorted(entries, key=lambda e: e.timestamp, reverse=True)

    streak = 0
    current_date = datetime.utcnow().date()

    for entry in sorted_entries:
        if entry.timestamp.date() == current_date - timedelta(days=streak):
            streak += 1
        else:
            break

    return streak
