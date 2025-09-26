
# Smart PMS – Basic Prototype

This is a minimal working prototype for the Smart Patient Management System (Registration, Booking, Dashboard).
Use it for Assessment 3 to demonstrate: repository management, project board, prototype, test plan, and QA.

## Run backend (Flask)
```bash
cd backend
pip install -r requirements.txt
python app.py
```
Server runs at `http://localhost:5000`

## Open frontend
Open `frontend/index.html` in your browser.
- Register a patient
- Book an appointment (use the same email)
- View patients/appointments on the Dashboard

## API endpoints
- `GET /health`
- `POST /register` { name, email }
- `GET /patients`
- `POST /book` { patient_email, date, time, doctor }
- `GET /appointments`

## Notes
- Data is stored in `backend/data.json` for demo purposes.
- Add PyTest tests in `backend/tests/` for extra marks.
- Push this folder to GitHub and create Issues/Branches/PRs for evidence.
```

