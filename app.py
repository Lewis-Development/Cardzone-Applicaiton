from flask import Flask, render_template, url_for, flash, redirect
from forms import loginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '75653e5973cb44730548299077a36e58'

@app.route("/", methods=['GET', 'POST'])
def home():
    form = loginForm()
    if form.validate_on_submit():
        if form.storeID.data == 1234 and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('/'))
        else:
            flash('Login unsuccessful. Please try again.', 'danger')
    return render_template('splash.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug = True)