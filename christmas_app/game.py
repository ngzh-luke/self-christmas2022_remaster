from flask import Blueprint, render_template, request, redirect, url_for,flash, abort, session
from flask_login import login_required, current_user, login_fresh
from .models import Game, Question, User
from ._tools_ import updateSessionTime
from . import db
from datetime import datetime, timezone

game = Blueprint('game', __name__)


@game.route("/game/")
def baseLandingForGame():
    updateSessionTime()
    if (current_user.is_authenticated):
        return redirect(url_for("game.loggedUser_gameLanding", user_alias=current_user.alias)) # redirect to logged in user game
    else:
        return redirect(url_for('game.guestUser_gameLanding'))

@game.route('/<string:user_alias>/have-fun-with-my-game/')
@login_required
def loggedUser_gameLanding(user_alias):
    session['current'] = '/' + str(current_user.alias) + '/have-fun-with-my-game/'
    return render_template('gameLanding.html', user=current_user,game=Game.query.all())

@game.route('/as-a-guest/have-fun-with-my-game/')
def guestUser_gameLanding():
    session['current'] = '/as-a-guest/have-fun-with-my-game/'
    try:
        if User.get_id(current_user):
            return redirect(url_for("game.loggedUser_gameLanding", user_alias=current_user.alias))
    except:
        pass
    return render_template('gameLanding.html', user=current_user, game=Game.query.all())

@game.route("/as-a-guest/have-fun-with-my-game/play/")
def guestUserPlay():
    session['current'] = '/as-a-guest/have-fun-with-my-game/play/'
    return render_template('gamePlay.html', user=current_user)

@game.route("/<string:user_alias>/have-fun-with-my-game/play/")
@login_required
def loggedUserPlay(user_alias):
    session['current'] = '/' + str(current_user.alias) + '/have-fun-with-my-game/play/'
    return render_template('gamePlay.html', user=current_user, user_alias=current_user.alias)

@game.route("/play/")
def play():
    try:
        if User.get_id(current_user):
            return redirect(url_for("game.loggedUserPlay", user_alias=current_user.alias))
    except:
        pass
    return redirect(url_for("game.guestUserPlay", user=current_user))

def onlyMe(template_name:str='questionsManager.html', **kwargs):
    if not current_user.is_authenticated:
        abort(401) # unauthorized
    elif current_user.isMe == True:
        return render_template(template_name, **kwargs)
    elif current_user.isMe != True:
        abort(403) # forbidden
    
@game.route("/question-manager/")
@login_required
def mng():
    return redirect(url_for('game.questionMng_Landing', user_alias=current_user.alias))

@game.route("/add/")
@login_required
def add():
    return redirect(url_for("game.questionMng_AddQ", user_alias=current_user.alias))

@game.route("/edit/")
@login_required
def edit():
    return redirect(url_for("game.questionMng_Query", user_alias=current_user.alias))

@game.route("/<string:user_alias>/have-fun-with-my-game/questions-management/", methods=['GET'])
@login_required
def questionMng_Landing(user_alias):
    return onlyMe(user=current_user) # auto render template
    
@game.route("/<string:user_alias>/have-fun-with-my-game/questions-management/query/", methods=['POST', "GET"])
@login_required
def questionMng_Query(user_alias):
    onlyMe(user=current_user) # just restrict the access
    if request.method == 'POST':
        id = request.form.get("new_question")
        question = Question.query.filter_by(q_id=id).first()
        session['question'] = question
        return redirect(url_for("game.questionMng_EditQ", user_alias=current_user.alias))
    return render_template('plain.html', user=current_user, query=True)

@game.route("/<string:user_alias>/have-fun-with-my-game/questions-management/add-question/", methods=['POST', "GET"])
@login_required
def questionMng_AddQ(user_alias):
    onlyMe(user=current_user) # just restrict the access
    if request.method == 'POST':
        new_question = request.form.get("new_question")
        answer = request.form.get('answer')
        question = Question()
        # try:
        #    db.session.add()
        #    db.session.commit()
        #    flash("Question has been added", category="success")
        # except:
        #   pass
        #
        
    return render_template('questionsManager.html', user=current_user, add=True)

@game.route("/<string:user_alias>/have-fun-with-my-game/questions-management/edit-question/", methods=['POST', "GET"])
@login_required
def questionMng_EditQ(user_alias):
    onlyMe(user=current_user) # just restrict the access
    if 'question' in session:
        if session['question'] == None:
            return redirect(url_for('game.add'))
    elif not 'question' in session:
        return redirect(url_for('game.add'))
    if request.method == 'POST':
        question = session['question']
        new_question = request.form.get("new_question")
        answer = request.form.get('answer')
        toBeEdited = question
        session['question'] = None # clear the question data
    return render_template('questionsManager.html', user=current_user, edit=True)


@game.route("/have-fun-with-my-game/answer-key/")
def answerKey():
    flash("Attention! Please complete the game before see the answer key", category='warning')
    return render_template("answerKey.html", user=current_user)

@game.route("/have-fun-with-my-game/submit/", methods=['POST'])
def submit():
    wenti = [1,2,3,4,5,6,7,8,9,10]
    corNum = int(0)
    if request.method == 'POST':
        wenti[0] = request.form.get("q1")
        wenti[1] = request.form.get("q2")
        wenti[2] = request.form.get("q3")
        wenti[3] = request.form.get("q4")
        wenti[4] = request.form.get("q5")
        wenti[5] = request.form.get("q6")
        wenti[6] = request.form.get("q7")
        wenti[7] = request.form.get("q8")
        wenti[8] = request.form.get("q9")
        wenti[9] = request.form.get("q10")
        for i in range(0,10):
            if wenti[i] == 'correct':
                corNum += 1
        if (current_user.is_authenticated):
            
            try:
                pts = Game(finish_at=datetime.now(),score=corNum, played_by=current_user.fname)
                db.session.add(pts)
                db.session.commit()
                flash(f"Good Job！You got {corNum}/10 points!", category='success')
                return redirect(url_for('game.baseLandingForGame', user=current_user))
            except:
                db.session.rollback()
            
        else:
            flash(f"Good Job！You got {corNum}/10 points! (Please note that guest user doesn't have score saving record)", category='success')
            return redirect(url_for('game.baseLandingForGame', user=current_user))
    return redirect(url_for('game.baseLandingForGame', user=current_user))