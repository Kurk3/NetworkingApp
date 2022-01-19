from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from src.import_db.tables import User, Contents

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("after_login/home.html", user=current_user)


@views.route('/zdroje', methods=['GET', 'POST'])
@login_required
def zdroje():
    return render_template("lectures/zdroje.html", user=current_user)

@views.route('/new_base', methods=['GET', 'POST'])
@login_required
def new_base():
    return render_template("after_login/home.html", user=current_user)

@views.route('/img_test', methods=['GET', 'POST'])
@login_required
def img_test():
    return render_template("after_login/image_test.html", user=current_user)



@views.route('/vysledky', methods=['GET', 'POST'])
@login_required
def vysledky():
    name_second_login = request.form.get('name')
    password_second_login = request.form.get('password')

    if request.method == 'POST':
        if name_second_login == "admin" and password_second_login == "admin":
            user_from_db = User.query.all()
            tests_from_db = Contents.query.all()
            headings = ('TEST', 'USER')
            # pridat cas uzivatela do aplikacie.

            print('uspesne si sa prihlasil')
            # presmerovanie na adresu az ked sa tento uzivatel znovu prihlasi.
            return render_template("after_login/table_of_tests.html",
                                   user=current_user,
                                   data=user_from_db,
                                   tests=tests_from_db,
                                   headings=headings,
                                   zip=zip)  # redirectne aktualneuzivatela
        else:
            print('nemas udaje k prihlaseniu')

    return render_template("after_login/second_login.html", user=current_user)
