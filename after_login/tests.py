from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from src import db
from src.import_db.tables import Contents

tests = Blueprint('tests', __name__)


@tests.route('/tests', methods=['GET', 'POST'])
@login_required  # toto to musi obsahovat.
def main_tests():
    print(current_user)
    return render_template('tests/tests.html', user=current_user)


@tests.route('/test1', methods=['GET', 'POST'])
@login_required
def test_num01():
    pocet_spravnych_odpovedi = 0
    question_1 = request.form.get('question1')
    question_2 = request.form.get('question1')
    question_3 = request.form.get('question2')
    question_4 = request.form.get('question2')
    question_5 = request.form.get('question2')
    question_6 = request.form.get('question2')
    question_7 = request.form.get('question2')
    question_8 = request.form.get('question2')
    question_9 = request.form.get('question2')
    question_10 = request.form.get('question2')


    if request.method == 'POST':
        if question_1 == 'answer2':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        if question_2 == 'answer2':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        if question_3 == 'answer3':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        if question_4 == 'answer1':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        if question_5 == 'answer1':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        if question_6 == 'answer3':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        if question_7 == 'answer3':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        if question_8 == 'answer3':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        if question_9 == 'answer2':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')

        if question_10 == 'answer1':
            print('tvoja odpoved je spravna')
            pocet_spravnych_odpovedi = pocet_spravnych_odpovedi + 1
        else:
            print('tvoja odpoved je nespravna')




        finale = pocet_spravnych_odpovedi / 10  * 100
        print('presmerovany na homepage/ test bol odoslany')
        print('vysledok testu je :', finale)

        user_answers = Contents(test=finale, user_id=current_user.id)

        exists = db.session.query(
            db.session.query(Contents).filter_by(user_id=current_user.id).exists()
        ).scalar()

        if exists:
            print('uzivatel v databaze uz existuje')
            return redirect(url_for('views.home', user=current_user))
        #returne na adresu kde bude napisane test si uz pisal pockaj na vysledok
        else:
            print('uzivatel neexistuje informacie budu pridane do databazy')
            db.session.add(user_answers)
            db.session.commit()
            return redirect(url_for('views.home', user=current_user))

    return render_template('tests/test_01.html', user=current_user)
