from flask import Flask, render_template, url_for
from forms import loginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '75653e5973cb44730548299077a36e58'

@app.route("/")
def home():
    return render_template('splash.html', title = 'Home')

@app.route("/login")
def login():
    form = loginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
    app.run(debug = True)