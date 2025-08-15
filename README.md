# MindBloom – Your Personal Mental Wellness Companion

#### Video Demo: [https://youtu.be/I-mDfifnGzY](https://youtu.be/I-mDfifnGzY)

## Overview
MindBloom is a mobile-friendly web application designed to help you take care of your mental wellness in a simple, accessible way. It provides a private space to journal your thoughts, track your mood, build healthy habits, and set personal goals. The goal is to create a supportive and secure digital environment where you can reflect, grow, and stay motivated.

This project is more than just a productivity tool. MindBloom is built to encourage regular self-check-ins, help you recognize patterns in your daily life, and provide tools that make personal growth achievable.

## Live Demo
You can try the app here: [https://sam0.pythonanywhere.com](https://sam0.pythonanywhere.com)

## Built With
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Python (Flask)
- **Database:** SQLite
- **Security:** CSRF protection, password hashing
- **Extensions:** Flask-SQLAlchemy, Flask-Login, Flask-Migrate, Flask-WTF

## Main Features

**Home Dashboard**  
The homepage welcomes you with a simple layout that introduces the main features and helps you navigate the app easily.

**User Authentication**  
Secure registration, login, and logout with password hashing. Users can manage their profile, change passwords, and switch between light and dark themes.

**Daily Journal**  
A private space to write entries with optional titles, tags, and mood indicators. Previous entries are stored in chronological order.

**Mood Tracker**  
Daily mood selection with space for notes and reflections. Tracks trends and streaks over time to help you understand your patterns.

**Habit Tracker**  
Create custom habits with set frequencies. Visual progress tracking and weekly summaries help you stay consistent.

**Goal Setting**  
Add personal goals with target dates and status tracking. A progress bar gives a quick overview of completion.

**Daily Affirmations**  
One positive affirmation is provided each day, with the option to add your own.

**About and Settings**  
An About page explains the purpose of the app. The settings modal allows you to adjust account details, privacy, notifications, and theme preferences. It also includes help documentation and a feedback form.

## Application Structure

MindBloom is built using the **application factory pattern** (`create_app()` function in `__init__.py`). This approach makes the project modular and easy to maintain.

**Extensions initialized:**
- `db` – SQLAlchemy ORM for database management
- `login_manager` – Handles user sessions and authentication
- `migrate` – Flask-Migrate for database schema changes
- `csrf` – CSRFProtect for form security

**Blueprints registered:**
- `main` – Home, settings, about, and feedback routes
- `auth` – Authentication (register, login, logout)
- `journal` – Journal entries
- `mood` – Mood tracking
- `habits` – Habit tracking
- `goals` – Goal management
- `affirmations` – Daily and custom affirmations

**Context Processors:**  
The app injects navigation items and social media links into all templates, so navigation menus are dynamic and easy to update.

## Database Structure
MindBloom uses SQLite for storage. The main tables are:
- **users** – Stores account details and preferences
- **journal_entry** – Journal entries
- **mood_entry** – Mood logs
- **habit** – Defined habits
- **habit_log** – Completed habit records
- **goal** – Goals with deadlines and status
- **affirmations** – Daily or custom affirmations
- **feedback** – Feedback submitted by users

## Folder and File Structure
The app’s structure:
- **app/** – Main application package
  - **main/** – Home, about, settings routes
  - **auth/** – Authentication routes
  - **journal/** – Journal feature
  - **mood/** – Mood tracker
  - **habits/** – Habit tracker
  - **goals/** – Goal setting
  - **affirmations/** – Daily affirmations
  - **templates/** – HTML templates
  - **static/** – CSS, JS, and images
  - `models.py` – Database models
  - `__init__.py` – App factory and blueprint registration
- **config.py** – App configuration (database URL, secret key, etc.)
- **requirements.txt** – Dependencies

## Security
- Passwords stored using secure hashing
- CSRF protection for all forms
- Minimal personal information stored
- Privacy controls for user data visibility

## Design Choices
- **Application factory pattern** for scalability and maintainability
- **Blueprints** for clean separation of features
- **SQLite** for simplicity and portability
- **Bootstrap** for responsive, mobile-friendly design

## Final Thoughts
MindBloom is designed to be approachable and useful for anyone looking to improve their mental wellness. It combines journaling, mood tracking, habit building, and affirmations into one space. The goal is to help users take small but meaningful steps toward a healthier mindset.

Whether you use it daily or once in a while, MindBloom can be a helpful companion in your personal growth journey.

**Live demo:** [https://sam0.pythonanywhere.com](https://sam0.pythonanywhere.com)
