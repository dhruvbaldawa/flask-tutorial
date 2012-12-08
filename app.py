from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsMySecretKey'


@app.route("/")
def index():
    return "Hello World"


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # This is executed when the user submits the form.
        username = request.form['username']
        password = request.form['password']
        # Check for superhumans
        if username == 'rajnikant' or username == 'chuck_norris':
            return 'Login successful'
        else:
            return 'Humans not allowed'

    else:
        # This is executed when the user visits the about route.
        return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
