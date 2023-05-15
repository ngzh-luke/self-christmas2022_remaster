""" Sever side of all views catagorized as customized views """
from flask import Blueprint, render_template, redirect, url_for, session, flash
from flask_login import current_user, login_required
from .models import User
from ._tools_ import updateSessionTime
from .msg import *

cusViews = Blueprint('cViews', __name__)


@cusViews.route('/customized-view/')
@login_required
def redirector():
    session['current'] = '/customized-view/'
    try:
        if User.get_id(current_user):
            alias = current_user.alias
            alias = alias.lower()
            try:
                return redirect(url_for("cViews."+alias))
            except:
                flash(
                    'Redirected to general view (likely because you do not have customized for you view)', category='info')
                return redirect(url_for('views.celebrate', user=current_user, user_alias=current_user.alias))
    except:
        pass
    return redirect(url_for('views.celebrate', user=current_user, user_alias=current_user.alias))


@cusViews.route('/for/admin/customized-celebration-view/')  # test view
# self (can't click the quick link button to access the page due to the redirect function)
@cusViews.route("/for/Kan/customized-celebration-view/")
@login_required
def admin():
    session['current'] = '/customized-view/'
    return "Customized view ^_^"


@cusViews.route("/for/Dad/customized-celebration-view/")  # dad
@login_required
def dad():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Dad':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("dad.html", user=current_user, title='just for Dad ^_^', msg_dad=msg_dad, msg_us=msg_us)


@cusViews.route("/for/Mom/customized-celebration-view/")  # mom
@login_required
def mom():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Mom':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("mom.html", user=current_user, title='just for Mom ^_^', msg_mom=msg_mom, msg_us=msg_us)


@cusViews.route("/for/Pa/customized-celebration-view/")  # pa
@login_required
def pa():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Pa':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("pa.html", user=current_user, title='just for Pa ^_^')


@cusViews.route("/for/Mama/customized-celebration-view/")  # mama
@login_required
def mama():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Mama':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("ma.html", user=current_user, title='just for Mama ^_^')


@cusViews.route("/for/Addy/customized-celebration-view/")  # addy
@login_required
def addy():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Addy':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("addy.html", user=current_user, title='just for Addy ^_^', msg_addy=msg_addy)


@cusViews.route("/for/Evander/customized-celebration-view/")  # evander
@login_required
def evander():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Evander':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("evander.html", user=current_user, title='just for Evander ^_^', msg_evander=msg_evander)


@cusViews.route("/for/AjTrithep/customized-celebration-view/")  # aj.trithep
@login_required
def ajtrithep():
    session['current'] = '/customized-view/'
    if current_user.alias != 'AjTrithep':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("ajTrithep_ajJade.html", user=current_user, title='just for Aj.Trithep ^_^')


@cusViews.route("/for/AjJade/customized-celebration-view/")  # aj.jade
@login_required
def ajjade():
    session['current'] = '/customized-view/'
    if current_user.alias != 'AjJade':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("ajTrithep_ajJade.html", user=current_user, title='just for Aj.Jade ^_^')


@cusViews.route("/for/Papa/customized-celebration-view/")  # papa
@login_required
def papa():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Papa':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("grandma_papa.html", user=current_user, title='just for Papa ^_^', msg=msg_gm_pp)


@cusViews.route("/for/Grandma/customized-celebration-view/")  # grandma
@login_required
def grandma():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Grandma':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("grandma_papa.html", user=current_user, title='just for Grandma ^_^', msg=msg_gm_pp)


@cusViews.route("/for/Kwan/customized-celebration-view/")  # kwan
@login_required
def kwan():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Kwan':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("kwan.html", user=current_user, title='just for Kwan ^_^', msg=msg_kwan)


@cusViews.route("/for/Wish/customized-celebration-view/")  # wish
@login_required
def wish():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Wish':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("wish.html", user=current_user, title='just for Wish ^_^', msg=msg_wish)


@cusViews.route("/for/Noemi/customized-celebration-view/")  # noemi
@login_required
def noemi():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Noemi':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("noemi.html", user=current_user, title='just for Noemi ^_^', msg=msg_noemi)


@cusViews.route("/for/Anna/customized-celebration-view/")  # anna
@login_required
def anna():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Anna':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("anna.html", user=current_user, title='just for Anna ^_^', msg=msg_anna)


@cusViews.route("/for/Candice/customized-celebration-view/")  # candice
@login_required
def candice():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Candice':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("candice.html", user=current_user, title='just for Candice ^_^', msg=msg_candice)
