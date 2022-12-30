from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)
master = Blueprint('main', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/logout')
def logout():
    return render_template('base.html')


@master.route('/')
def index():
    return render_template('index.html')


@master.route('/profile')
def profile():
    return render_template('profile.html')
