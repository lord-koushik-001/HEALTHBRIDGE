# HealthBridge

A medical camp registration portal built to help people in South India find and register for free healthcare camps. No documents required, no fees, no barriers.

---

## About

HealthBridge started as a simple idea — make it easier for people to access free medical checkups without the usual friction of paperwork and queues. The platform lists upcoming camps, lets visitors register in under a minute, and gives organisers a dashboard to track who's coming.

Six camps are running across South India between June and July 2026, covering general health, eye care, dental, blood donation, cardiac screening, and sports injuries. All of them are free and open to everyone.

---

## Pages

- **Home** — overview of the initiative, how it works, upcoming camps, and FAQs
- **Camps** — full list of camps with search and filters by category, city, date, and age group
- **Register** — simple form to sign up for a camp
- **About** — background on the project
- **Contact** — contact details
- **Admin** — internal dashboard showing all registrations

---

## Stack

- Python + Flask
- SQLite
- HTML / CSS (no frameworks)

---

## Running Locally

```bash
git clone https://github.com/YOUR_USERNAME/medical-camp-portal.git
cd medical-camp-portal
pip install flask
python3 app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## Admin Dashboard

Go to `/admin` to see all registered participants, their details, and the IP address of their registration.

---

## Project Structure

```
medical-camp-portal/
├── app.py
├── database.db
├── requirements.txt
├── static/
│   ├── style.css
│   └── venti-views-unsplash.jpg
└── templates/
    ├── home.html
    ├── camps.html
    ├── register.html
    ├── success.html
    ├── about.html
    ├── contact.html
    └── admin.html
```

---

Built by Koushik Venkatesan — 2026
