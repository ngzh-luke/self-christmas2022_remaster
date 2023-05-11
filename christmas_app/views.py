""" Sever side of all views catagorized as general views """
from flask import Blueprint, render_template, redirect, url_for, session, request, abort
from christmas_app import systemInfoObject
from flask_login import current_user
from .models import User
from ._tools_ import updateSessionTime
import time

views = Blueprint('views', __name__)


@views.route('/')
def landing():
    # try:
    #     if User.get_id(current_user):
    #         return redirect(url_for("features.c", user_id=current_user.fname)) # redirect to cake page
    # except:
    #     pass
    session['current'] = '/'
    updateSessionTime()
    return render_template('landing.html', user=current_user)


@views.route('/joy-is-arrived/')
def celebrate():
    session['current'] = '/joy-is-arrived/'
    updateSessionTime()
    return render_template('celebration.html', user=current_user)


@views.route('/about/')
def about():
    session['current'] = '/about/'
    updateSessionTime()
    return render_template('about.html', user=current_user, ab=systemInfoObject)


@views.route("/set-session-lang/", methods=['POST', "GET"])
def setLang():
    if not 'LANG' in session:
        session['LANG'] = 'EN'
    if request.method == 'POST':
        if session['LANG'] == 'EN':
            session['LANG'] = 'TH'
        else:
            session['LANG'] = 'EN'
    time.sleep(1.5)
    if 'current' in session:
        if (session['current'] == "/logout"):
            return redirect(url_for('auth.logIn'))
        else:
            return redirect(session['current'])
    else:
        session['LANG'] = 'EN'
        return redirect(url_for('auth.logIn'))
