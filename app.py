from flask import Flask, request, render_template, session, redirect, url_for
from models import User

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsMySecretKey'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # This is executed when the user submits the form.
        username = request.form['username']
        password = request.form['password']

        status, message = User.authenticate(username, password)

        if status:
            # Setup the session variables
            session['user_name'] = message['name']
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return 'Login unsuccessful'

    else:
        # This is executed when the user visits the above route.
        return render_template('login.html')
@app.route("/logout")
def logout():
    # Destroy the session variables
    session.pop('user_name', None)
    session.pop('logged_in', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
