from flask import Flask, render_template, request, url_for, redirect, session
from flask_bootstrap import Bootstrap

from flask_mysqldb import MySQL
from spotipy.oauth2 import SpotifyOAuth
import time

"""
from jinja2 import Environment, FileSystemLoader


template_dir = '/frontend/src/app'
env = Environment(loader=FileSystemLoader(template_dir))
"""

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'clavesecreta'

app.config['SESSION_COOKIE_NAME'] = 'My apps cookies'
TOKEN_INFO = "token_info"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'myplaylists'

mysql = MySQL(app)
posts = []


@app.route("/")
def index():
    return render_template("index.html", num_posts=len(posts))


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (alias, email, contrasenia) VALUES (%s, %s, %s)', (username, email, password))
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
    return render_template('main.html')


@app.route('/userprofile')
def userprofile():
    return render_template('userprofile.html')


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id='29f753bf79c244d4a27965c1ae47946a',
        client_secret='683f0860d10c49e3a3359242169fae7b',  #Esto NO tiene que quedar guardado en git
        redirect_uri=url_for('main.html', _external=True),
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
