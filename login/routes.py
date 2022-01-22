from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_bootstrap import Bootstrap
from flask_login import login_user, login_required, logout_user
from forms import LoginForm, SignupForm
from flask_mysqldb import MySQL

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'clavesecreta'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '630667'
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuario (username, email, password) VALUES (%s, %s, MD5(%s))', (username, email, password))
        mysql.connection.commit()
    return render_template('login.html', form=form)

@app.route('/signout')
@login_required
def signout():
    logout_user()
    flash('Sesión de usuario cerrada')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)