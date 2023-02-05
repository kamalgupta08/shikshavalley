from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from shikshavalley.extensions import db
from shikshavalley.models import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['username']
        unhashed_password = request.form['password']

        user = User(
            name=name,
            unhashed_password=unhashed_password,
            admin=True,
            teacher=False,
            student=False
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():

    error_message = None

    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()

        if not user or not check_password_hash(user.password, password):
            error_message = 'Invalid Credentials. Please try again.'
            flash(error_message)

        if not error_message:
            login_user(user)
            return redirect(url_for('admin.search'))

    return render_template('login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))