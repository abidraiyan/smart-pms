# Smart Patient Management System (Smart PMS)

Prototype system for hospital management workflows: registration, booking, dashboard, chatbot.

## Structure

- `frontend/` - HTML/CSS/JS prototype UI
- `backend/` - Flask API with JSON storage
- `.github/workflows/ci.yml` - GitHub Actions pipeline

## Run Backend
```
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Backend runs at http://127.0.0.1:5000

## Run Frontend
Open `frontend/login.html` in browser or run:
```
cd frontend
python -m http.server 8080
```

## Demo Credentials
- Username: admin
- Password: 1234

## Features
- Patient registration
- Appointment booking
- Staff dashboard
- AI chatbot for FAQs
- Login/logout navigation

## Notes
Prototype only; future iteration uses Django + React + PostgreSQL.
