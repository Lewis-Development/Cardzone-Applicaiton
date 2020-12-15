from flask import Flask, render_template, url_for, flash, redirect
from forms import loginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '75653e5973cb44730548299077a36e58'

@app.route("/", methods=['GET', 'POST'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if form.storeID.data == 1 and form.password.data == '1':
            return redirect(url_for('login'))
    return render_template('login.html', title='Login', form=form)

def home():
    return render_template('home.html', title='Home')

if __name__ == '__main__':
    app.run(debug = True)