import os
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
@app.after_request
def add_ngrok_header(response):
    response.headers['ngrok-skip-browser-warning'] = 'true'
    return response
# Create Database and Table
def init_db():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS registrations(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        phone TEXT,
        email TEXT,
        camp TEXT,
        ip_address TEXT
    )
    ''')

    conn.commit()
    conn.close()


# Home Page
@app.route('/')
def home():
    return render_template('home.html')


# Camp Details Page
@app.route('/camps')
def camps():
    return render_template('camps.html')

@app.route("/about")
def about():
    return render_template("about.html")


# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        email = request.form['email']
        camp = request.form['camp']
        ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO registrations
        (name, age, phone, email, camp, ip_address)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, age, phone, email, camp, ip_address))

        conn.commit()
        conn.close()

        return render_template(
            'success.html',
            name=name,
            camp=camp
        )

    return render_template('register.html')


# Admin Dashboard
@app.route('/admin')
def admin():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM registrations')
    participants = cursor.fetchall()

    cursor.execute('SELECT COUNT(*) FROM registrations')
    total_registrations = cursor.fetchone()[0]

    conn.close()

    return render_template(
        'admin.html',
        participants=participants,
        total_registrations=total_registrations
    )
    

# Initialize Database
init_db()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)