from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import LoginForm, SignUpForm
from flask_login import login_required, login_user, logout_user, current_user
from . import db
from .models import Users
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__) 

#Auth route for user login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect(url_for('views.index'))
            else:
                flash('Invalid email or password.')
    return render_template('auth/login.html', form=form)

#Auth route for user sign-up
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    status = 0
    if request.method == "POST":
        if form.validate_on_submit():
            print(if_email_exists(form.email.data))
            if if_email_exists(form.email.data):
                new_user = Users(email=form.email.data,
                                    password=generate_password_hash(form.password.data),
                                    first_name=form.first_name.data,
                                    last_name=form.last_name.data)
                db.session.add(new_user)
                db.session.commit()
                flash('Your user registration was successful.')
                status=1
            else:
                flash('Email already exists.', 'custom')
                status=0
        else:
            if form.errors:
                for error in form.errors.values():
                    flash(error)
                    status=0
                
    return render_template('auth/sign-up.html', form=form, status=status)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.index'))

def if_email_exists(email):
    """Functions that checks if a specific email is already used/already exists
    
    :param email: the email to be checked
    """
    email = Users.query.filter_by(email=email).first()
    if email is None:
        return True
    return False