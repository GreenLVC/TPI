from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_bootstrap import Bootstrap
from flask_login import login_required, logout_user
from forms import LoginForm, SignupForm
from flask_mysqldb import MySQL
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'clavesecreta'

app.config['SESSION_COOKIE_NAME'] = 'My apps cookies'
TOKEN_INFO = "token_info"

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

@app.route('/loginSpotify')
def loginSpotify():
    sp_oaut = create_spotify_oauth()
    auth_url = sp_oaut.get_authorize_url()
    return redirect(auth_url)

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
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/signupSpotify')
def signupSpotify():
    sp_oaut = create_spotify_oauth()
    auth_url = sp_oaut.get_authorize_url()
    return redirect(auth_url)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/main')
def main():
    sp_oaut = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oaut.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('main', _external=True))


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id='29f753bf79c244d4a27965c1ae47946a',
        client_secret='secret',  #Esto NO tiene que quedar guardado en git
        redirect_uri=url_for('index', _external=True),
        scope='user-read-private user-read-email user-library-read playlist-modify-private playlist-read-private'
    )

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        return redirect(url_for('login', _external=True))
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
        sp_oaut = create_spotify_oauth()
        token_info = sp_oaut.get_refresh_access_token(token_info['refresh_token'])
    return token_info

if __name__ == '__main__':
    app.run(debug=True)