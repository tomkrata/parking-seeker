from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from model.user import User
from service.user_service import user_exists, insert_user, fetch_user

auth = Blueprint('auth', 'controller.user_controller')
master = Blueprint('main', 'controller.user_controller')
par = Blueprint('par', 'controller.user_controller')


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = fetch_user(email)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user['password'], password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if the user doesn't exist or password is wrong, reload the page
    # if the above check passes, then we know the user has the right credentials
    session['username'] = user['username']
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user_found = user_exists(email)
    if user_found:  # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    ret = insert_user({'username': name, 'password': generate_password_hash(password, method='sha256'), 'email': email})
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    session['username'] = None
    return render_template('login.html')


@master.route('/')
def index():
    return render_template('index.html')


@par.route('/park')
def park():
    # if session['username'] is None:
    #     flash('You are not signed in, the parking api will not work!')
    return render_template('parking.html')


@master.route('/profile')
def profile():
    return render_template('profile.html', user=session['username'])
