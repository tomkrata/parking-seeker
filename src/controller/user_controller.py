from flask import Blueprint, render_template, request, redirect, url_for

from model.user import User
from service.user_service import user_exists, insert_user

auth = Blueprint('auth', 'controller.user_controller')
master = Blueprint('main', 'controller.user_controller')


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user_found = user_exists(email)
    if user_found: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))
    ret = insert_user({'username': name, 'password': password, 'email': email})
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return render_template('login.html')


@master.route('/')
def index():
    return render_template('index.html')


@master.route('/profile')
def profile():
    return render_template('profile.html')
