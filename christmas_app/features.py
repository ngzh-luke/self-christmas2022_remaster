from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from .models import User
from ._tools_ import updateSessionTime
from . import systemInfo

features = Blueprint('features', __name__)


def checker() -> None:
    if request.method == "POST":
        account_ = request.form.get('account_').upper()
        if account_ is not None:
            user = User.query.filter_by(fname=account_).first()
            if user is not None:
                user_fname = user.fname
                if user_fname == account_:
                    flash('You may use your first name to login.',
                          category='found')

            else:
                flash(
                    "However, you still can enjoy the present without logged in ^_^", category='not found')
        else:
            flash("However, you still can enjoy the present without logged in ^_^",
                  category='not found')


@features.route("/<string:user_alias>/cake/")
@login_required
def cake(user_alias):
    session['current'] = '/' + str(current_user.alias) + '/cake/'
    updateSessionTime()
    return render_template('cake.html', user=current_user)


@features.route("/cake/")
@login_required
def redirector():
    return redirect(url_for('features.cake', user_alias=current_user.alias))


@features.route('/check-account/by-first-name/', methods=['POST'])
def independantChecker():
    updateSessionTime()
    checker()
    session['independantChecker'] = 'checked'
    return redirect(url_for('features.independantCheckerLanding'))


@features.route('/check-account/', methods=['GET'])
def independantCheckerLanding():
    session['current'] = '/check-account/'
    updateSessionTime()
    if 'independantChecker' in session and session['independantChecker'] == 'checked':
        session.pop('independantChecker', None)
        return render_template('checker.html', user=current_user, auto=False)
    else:
        return render_template('checker.html', user=current_user, auto=True)


@features.route("/game/")
def baseLandingForGame():
    session['current'] = '/game/'
    updateSessionTime()
    try:
        if User.get_id(current_user):
            # redirect to logged in user game
            return redirect(url_for("game.loggedUser_gameLanding", user_alias=current_user.alias))
    except:
        pass
    return redirect(url_for('game.guestUser_gameLanding'))


@features.get('/return-christmas2022remaster-app-info')
def getAppInfo():
    updateSessionTime()
    return str(systemInfo)
