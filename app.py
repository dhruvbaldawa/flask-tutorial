from flask import Flask, request, render_template, session, redirect, url_for, flash
from models import User


def create_app():
    ''' To create the application object, and initialize all the extensions
    and configurations
    '''
    app = Flask(__name__)
    app.config.from_object('config.Config')
    return app

app = create_app() # Create the application

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
            flash("Hello %s, %s" % (message['name'], message['message']), 'success')
            return redirect(url_for('index'))
        else:
            flash(message['message'], 'error')
            return redirect(url_for('login'))

    else:
        # This is executed when the user visits the above route.
        return render_template('login.html')

@app.route("/logout")
def logout():
    # Destroy the session variables
    session.pop('user_name', None)
    session.pop('logged_in', None)
    flash('You have been logged out successful', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
