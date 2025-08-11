# Mindbloom
Mobile Diary Project
This is Mindloom, a diary-like project that allows you to record, plan, and manage your day, wherever you are.
it is made of HTML, CSS, BOOTSTRAP, JS, SQLITE DB AND PYTHON(FLASK).
it is composed of several files in several folders as explained below.

Mindbloom contains a home page that introduces the app and explains its navigation.
log in and register that allows you to have and access your account so that you may use/access the following.
journal page allowing you to enter and store your ideas.
Mood Tracker page allowing you to track your mood, what triggers it,offering you insights,an affirmation, tomorrow's outlook and a daily question.
Habits page enabling you to write down your habits, edit, store, track,  and get a weekly overview of them. With suggestions of habits to adopt.
Goals page allowing you to set goals, track progress and get stats of all your goals and also suggestions provided.
Affirmations page with a daily affirmation(text and audio), allowing you to reflect on it and also add your own affirmations.
About page with all basic info for the users and visitors of the app.
and finally for the frontend comes a drop down that allows you to access various settings including account, notifications, privacy and theme-related related via a modal,toggle dark mode,access help center,send feedback,edit profile,change password and logout.

for the backend 
The app has files and folders that manage sessions, migrations, working environment, configuration(py) and app folder having the following:
affirmations,auth,goals,habits, and journal each one havung __init__.py and routes.py that manages the operations of their respective pages and route.
and a main folder to handle home page and the routes for about,settings,homepage,feedbackand their respective operations.
Then a static folder holding the general css for the app.
Templates folder holding the about,goals,affirmations,habits,help,index,journal,layout,login,mood and register HTML files and modals folder holding feedback and settings html modals.
__init.py and Models.py to create and manage the whole app.
And the app uses a sqlite database with the following: 
users
Fields: id, username, email, password_hash, display_name, email_visible, theme_preference, etc.

Description: Stores user credentials, preferences, and notification settings.

📓 journal_entry
Fields: id, user_id, title, content, tags, mood, date

Description: Personal journal entries with optional mood and tags.

😊 mood_entry
Fields: id, user_id, mood, notes, tags, reflection, timestamp

Description: Daily mood tracking with reflections and notes.

🔁 habit
Fields: id, user_id, name, category, frequency, created_at

Description: Defines recurring habits and their categories.

✅ habit_log
Fields: id, user_id, habit_id, completed_at

Description: Logs each time a habit is completed.

🎯 goal
Fields: id, user_id, title, description, target_date, status, created_at

Description: Tracks personal goals and their progress.

💬 affirmations
Fields: id, text, created, user_id

Description: Positive affirmations saved by the user.

feedback
Fields: id, user_id, message, category, created_at, status

Description: User-submitted feedback or suggestions.
the app also uses csrf protection,hashed passwords.

link to the web "https://sam0.pythonanywhere.com"

Fields: id, user_id, message, category, created_at, status

Description: User-submitted feedback or suggestions.
