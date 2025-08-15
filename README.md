# MindBloom – Your Personal Mental Wellness Companion

#### Video Demo: [<https://youtu.be/I-mDfifnGzY>](https://youtu.be/I-mDfifnGzY)

## Overview
MindBloom is a mobile-friendly web application designed to help you take care of your mental wellness in a simple, accessible way. It gives you a space to journal your thoughts, track your mood, build healthy habits, and set personal goals, all in one place. The app is meant to feel safe, private, and supportive, so you can focus on reflection, growth, and overall well-being.

I wanted this project to be more than just a productivity tool. MindBloom is built to encourage regular check-ins with yourself, help you recognize patterns in your mood and habits, and keep you motivated toward positive changes in your life.

## Live Demo
You can try the app here: [https://sam0.pythonanywhere.com](https://sam0.pythonanywhere.com)

## Built With
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Backend: Python (Flask)
- Database: SQLite
- Security: CSRF Protection and secure password hashing

## Main Features

**Home Dashboard**  
The homepage welcomes you and gives a clear overview of the app’s main features, helping you navigate easily.

**User Authentication**  
You can register for an account, log in securely, and manage your profile. There’s also an option to change your password and switch between light and dark themes.

**Daily Journal**  
A private place to record your thoughts, reflections, or ideas. You can give entries titles, add tags, and note your mood for that day. Past entries are stored in chronological order for easy browsing.

**Mood Tracker**  
Each day, you can select your mood, write about what influenced it, and respond to reflection prompts. The app tracks trends and streaks, helping you notice changes over time.

**Habit Tracker**  
Create and track your habits. You can choose how often you want to do them and check your progress visually. The app also gives you a weekly summary to keep you motivated.

**Goal Setting**  
Add your goals, set target dates, and track their progress. Goals can be marked as open, in progress, or past due, and you’ll see a progress bar to help you stay on track.

**Daily Affirmations**  
You’ll receive one daily affirmation, and you can add your own personal affirmations as well. The idea is to give you small, positive reminders to keep your mindset healthy.

**About and Settings**  
There’s an About page explaining the purpose behind the app and a settings modal where you can manage account details, privacy, themes, and notifications. You can also find help documentation and a feedback form here.

## Database Structure
MindBloom uses SQLite to store and organize data. The main tables include:

- **users** – Account details and preferences
- **journal_entry** – Journal entries with title, content, tags, and mood
- **mood_entry** – Mood logs with notes and reflections
- **habit** – User-defined habits
- **habit_log** – Records of completed habits
- **goal** – Goals with description, target dates, and status
- **affirmations** – Daily or custom affirmations
- **feedback** – Feedback messages from users

## Folder and File Structure
The app is organized using Flask blueprints, so each feature is handled in its own folder. Inside each feature folder:
- `__init__.py` initializes the module
- `routes.py` contains the feature-specific routes

Other important parts of the project:
- **main/** – Routes for homepage, settings, about, and feedback
- **static/** – CSS and JavaScript files
- **templates/** – HTML templates and modals
- **models.py** – Database models
- **__init__.py** (root) – Main app setup and configuration

## Security
Passwords are stored using secure hashing, and CSRF protection is used to keep form submissions safe. Personal information is kept private, and users have control over what is visible.

## Design Choices
I used Flask blueprints to make the app modular and easier to maintain. SQLite was chosen because it’s lightweight and perfect for this type of personal data tracking. Bootstrap ensures that the app is mobile-friendly, and the theme toggle lets users choose the look they’re most comfortable with.

## Final Thoughts
MindBloom was built with the idea that mental wellness tools should be simple, approachable, and helpful without feeling overwhelming. It combines journaling, mood tracking, habit building, and affirmations into one space so users can see their progress and reflect on their personal journey.

Whether you use it daily or a few times a week, I hope MindBloom can be a companion in helping you take small, meaningful steps toward a healthier mindset.

**Live demo:** [https://sam0.pythonanywhere.com](https://sam0.pythonanywhere.com)
