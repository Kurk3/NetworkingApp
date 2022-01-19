from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from src import db
from src.import_db.tables import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    print('metoda sa spustila')

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                print('prihlasenie bolo uspesne')
                login_user(user, remember=True)
                print('uspesne si sa prihlasil')
                return redirect(url_for('views.new_base'))

            else:

                print('zle heslo skus znovu')

        else:

            print('tento email neexistue')

    return render_template("before_login/login_4.html", user=current_user)


# login##########################################################################################

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# logout##########################################################################################

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already in use.', category='error')
            print('email sa uz pouziva pouzi ini email')
        elif len(email) < 4:
            print('email musi byt dlhsi ako 4 charaktery')
        elif len(first_name) < 2:
            print('Meno musi mat viac ako 1 charakter')
        elif password1 != password2:
            print('hesla sa nezhoduju')
        elif len(password1) < 7:
            print('heslo musi byt dlhsie ako 7 char')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()  # 'potvrdenie'
            login_user(new_user, remember=True)
            print('account was created!')
            return redirect(url_for('views.home'))

    return render_template("before_login/new_register.html", user=current_user)

@auth.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('before_login/homepage.html')