from app import app, lm
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required

@lm.user_loader
def load_user(id)
  # Add data-base support
  return 0

@app.route('/login', methods = ['GET', 'POST'])
def login():
  if g.user is not None and g.user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
    account = request.form.get('account')
    passwrd = request.form.get('passwrd')
    user = User.query.filter_by(account = account, passwrd = passwrd)
    if user is None:
      flash('Invalid Login, Please try again')
      return redirect(url_for('login'))
    g.user = user
    login_user(user)

    next = request.args.get('next')
    # next_is_valid should be checken if the user has been valid.
    # or the app may be attacked.
    if not next_is_valid(next):
      return flask.abort(400)

    return redirect('index')
  return render_template('login.html',
      title = 'Sign In',
      form = form)

@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect('login')