""" account manager """
from flask import redirect, render_template, Blueprint, url_for, request, flash, session
from flask_login import current_user, login_required, fresh_login_required
from flask_bcrypt import check_password_hash, generate_password_hash
from ._tools_ import updateSessionTime
from .models import User
from . import db

account = Blueprint('acc', __name__)

@account.route('/<string:user_alias>/account-management/', methods=["GET"])
@fresh_login_required
def manager(user_alias):
    session['current'] = '/' + str(current_user.alias) + '/account-management/'
    updateSessionTime()
    if 'risk' in session:
        data = session['risk']
    else:
        data = None
    return render_template('account.html', user=current_user, auto=False, data=[current_user.fname, current_user.alias,data])

@account.route('/<string:user_alias>/account-management/change-password/', methods=['POST','GET'])
@fresh_login_required
def changePS(user_alias):
    session['current'] = '/' + str(current_user.alias) + '/account-management/change-password/'
    updateSessionTime()
    if request.method == 'POST':
        current = request.form.get("current")
        new = request.form.get('new')
        confirmNew = request.form.get('confirmNew')
        u = User.query.filter_by(alias=user_alias).first()
        if check_password_hash(current_user.password, current):
            if (new == None or new == '') or (confirmNew == None or confirmNew == ''):
                flash("Neither new password can be empty nor the system can confirm new password", category='error')
                return redirect(url_for("acc.manager", user_alias=current_user.alias))
            elif (new == confirmNew):
                updated = generate_password_hash(new).decode('utf-8')
                u.password = updated
                db.session.commit()
                flash("Password successfully changed", category="success")
                return redirect(url_for("acc.manager", user_alias=current_user.alias))
            flash("New passwords not matched, please try again!", category='error')
            return redirect(url_for("acc.manager", user_alias=current_user.alias))
        flash("Can't confirm your identity, please try again! (current password is incorrect!)", category='error')
        return redirect(url_for("acc.manager", user_alias=current_user.alias))
    if 'risk' in session:
        data = session['risk']
    else:
        data = None
    return render_template('account.html', user=current_user, auto=True, data=[current_user.fname, current_user.alias,data])

@account.route('/wanna-change-password/')
@login_required
def redirector():
    return redirect(url_for('acc.changePS', user_alias=current_user.alias))

@account.route('/my-account/')
@login_required
def redirector_mng():
    return redirect(url_for('acc.manager', user_alias=current_user.alias))