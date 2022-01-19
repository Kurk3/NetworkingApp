from flask import Blueprint, render_template
from flask_login import login_required, current_user

lectures = Blueprint('lectures', __name__)


@lectures.route('/lectures')
@login_required
def main_lectures():
    return render_template('lectures/lectures_main.html', user=current_user)

@lectures.route('/historia_sieti')
@login_required
def lecture_num1():
    return render_template('lectures/lecture_02.html', user=current_user)

@lectures.route('/pocitacove_siete')
@login_required
def lecture_num2():
    return render_template('lectures/lecture_03.html', user=current_user)

@lectures.route('/referencny_model')
@login_required
def lecture_num3():
    return render_template('lectures/lecture_04.html', user=current_user)

@lectures.route('/iso_osi_model')
@login_required
def lecture_num4():
    return render_template('lectures/lecture_05.html', user=current_user)

@lectures.route('/tcp_ip_model')
@login_required
def lecture_num5():
    return render_template('lectures/lecture_06.html', user=current_user)

@lectures.route('/osi_vs_tcp_ip_packet_transfer')
@login_required
def lecture_num6():
    return render_template('lectures/lecture_07.html', user=current_user)

@lectures.route('/sietova_vrstva')
@login_required
def lecture_num7():
    return render_template('lectures/lecture_08.html', user=current_user)

@lectures.route('/ip_adresy')
@login_required
def lecture_num8():
    return render_template('lectures/lecture_09.html', user=current_user)

@lectures.route('/podsiete')
@login_required
def lecture_num9():
    return render_template('lectures/lecture_10.html', user=current_user)

@lectures.route('/mac_adresy')
@login_required
def lecture_num10():
    return render_template('lectures/lecture_11.html', user=current_user)

@lectures.route('/ipv6_adresy')
@login_required
def lecture_num11():
    return render_template('lectures/lecture_12.html', user=current_user)

@lectures.route('/sietove_topologie')
@login_required
def lecture_num12():
    return render_template('lectures/lecture_13.html', user=current_user)

@lectures.route('/sietove_komponenty')
@login_required
def lecture_num13():
    return render_template('lectures/lecture_14.html', user=current_user)

@lectures.route('/linkova_vrstva')
@login_required
def lecture_num14():
    return render_template('lectures/lecture_15.html', user=current_user)

@lectures.route('/fyzicka_vrstva')
@login_required
def lecture_num15():
    return render_template('lectures/lecture_16.html', user=current_user)

@lectures.route('/protokoly')
@login_required
def lecture_num16():
    return render_template('lectures/lecture_17.html', user=current_user)


