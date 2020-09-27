from flask import render_template, redirect, url_for
from datetime import datetime
from app import app, db, login_manager
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm
from .models import User

global user_last_login

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Login Page
@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                login_user(user)
                user_last_login = user.last_login
                user.last_login = str(datetime.now())
                db.session.commit()
                return redirect(url_for('home'))
        return 'Invalid Credentials'
    return render_template('login.html', form=form)

# Home Page
@app.route('/home')
@login_required
def home():
    user = {'last_seen': current_user.last_login, 'username':current_user.username}
    current_user.last_login = str(datetime.now())
    db.session.commit()
    return render_template('home.html', user=user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# user = User.query.filter_by(username='abdullah').first()
# login_user(user)
# user_info = {'username': user.username, 'id':user.id, 'last_login': user.last_login}
# user.last_login = str(datetime.now())
# db.session.commit()