MindBloom – Your Personal Mental Wellness Companion
MindBloom is a thoughtfully designed, mobile-friendly web app that empowers users to manage and enhance their mental wellness on the go. Whether you’re jotting down thoughts in your journal, tracking your daily mood, building healthy habits, or setting personal goals, MindBloom offers a safe and supportive digital space to help you reflect, grow, and thrive.

🔗 Live Demo: Visit MindBloom on PythonAnywhere

🛠️ Built With
Frontend: HTML, CSS, JavaScript, Bootstrap

Backend: Python (Flask)

Database: SQLite

Security: CSRF Protection, Password Hashing for secure login and data handling

✨ Key Features
🏠 Home Page
The home dashboard gives users a warm welcome and introduces each feature in a user-friendly way, helping them navigate the app smoothly.

🔐 User Authentication
Users can register and log in securely. They can also manage their accounts, including changing passwords, editing profiles, and toggling between light/dark themes—all from a clean dropdown modal.

📓 Daily Journal
A space to capture your thoughts, ideas, or reflections.

Add optional titles, tags, and moods

Browse previous entries chronologically

Great for mental clarity, creativity, and stress relief

😊 Mood Tracker
Track how you're feeling each day with:

Simple mood selection (e.g., Happy, Sad, Tired)

Space to describe events or triggers

Reflection prompts to deepen awareness

Visual stats including trends and mood streaks

Daily affirmation and outlook for tomorrow

🔁 Habit Tracker
Form and maintain healthy habits using:

Custom habit creation with categories and frequencies

Visual progress tracking and streaks

Weekly performance summary

Built-in habit suggestions to inspire consistency

🎯 Goal Setting
Define your goals and keep track of them effortlessly:

Add goals with due dates and status tracking (Open, In Progress, Past Due)

Progress bar and stats overview

Suggestions like “Run a 10K” or “Start a journaling habit” to keep you moving forward

💬 Daily Affirmations
Read or listen to uplifting affirmations to shift your mindset:

One provided daily

Option to add your own personal affirmations

Reflect on what resonates with you

ℹ️ About Page
Provides details about the app’s purpose, the mental wellness philosophy behind it, and ways to get in touch for feedback or collaboration.

⚙️ App Settings & Help Center
A modal lets users access:

Account details

Privacy and theme settings

Notifications

Help documentation

Send feedback directly via a feedback form

🧠 Database Structure (SQLite)
The database is structured to support seamless user experience and secure data handling:

👤 users
Stores basic user info and preferences.
Fields: id, username, email, password_hash, display_name, email_visible, theme_preference

📓 journal_entry
User journal data.
Fields: id, user_id, title, content, tags, mood, date

😊 mood_entry
Mood tracking log.
Fields: id, user_id, mood, notes, tags, reflection, timestamp

🔁 habit
User habits definition.
Fields: id, user_id, name, category, frequency, created_at

✅ habit_log
Each time a user completes a habit.
Fields: id, user_id, habit_id, completed_at

🎯 goal
Tracks user goals and milestones.
Fields: id, user_id, title, description, target_date, status, created_at

💬 affirmations
Daily or custom affirmations.
Fields: id, text, created, user_id

📝 feedback
Feedback submitted through the form.
Fields: id, user_id, message, category, created_at, status

📁 Folder & File Structure
MindBloom is built with modular Flask architecture. Each feature (journal, mood, goals, habits, affirmations, auth) is handled in separate blueprints with:

__init__.py: Initializes the module

routes.py: Manages feature-specific routes

Other notable folders:

main: Contains routes for homepage, settings, about, and feedback

static: Holds global CSS files

templates: Contains all HTML files including layout and modals

models.py: Defines all database tables

__init__.py (root): Sets up the Flask app, configurations, and database

🔒 Security & Best Practices
User passwords are hashed using secure algorithms

CSRF protection ensures safe form handling

Private user information is handled with care, with options for display preferences

💡 Final Thoughts
MindBloom is more than just a planner or tracker—it's a holistic space for reflection, emotional regulation, and personal growth. Built with simplicity and well-being in mind, it's perfect for anyone looking to become more intentional about their mental wellness.

🔗 Try it live now: https://sam0.pythonanywhere.com

Feel free to fork, contribute, or give feedback!
