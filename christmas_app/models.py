# Database schema
import datetime
import time

from flask_login import UserMixin, current_user, AnonymousUserMixin

from . import db


class User(db.Model, UserMixin, AnonymousUserMixin):
    """ Database table: user
        each user account setting/properties defined here.

        #Attribute:
            fname -> first name,
            alias -> alias (not null),
            password -> password,
            points -> foreign key to Game table
        """
    id = db.Column(db.Integer(), unique=True, primary_key=True)
    fname = db.Column(db.String(56), unique=True)  # first name
    alias = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String())
    points = db.relationship('Game')
    langPref = db.Column(db.String(2), default="EN")

    def __str__(self):
        return self.fname

    @property
    def isMe(self) -> bool:
        if not current_user.is_authenticated:
            # return current_app.login_manager.unauthorized()
            return False
        elif current_user.is_authenticated and (current_user.fname == 'KITTIPICH'):
            return True
        return False

    # Should be implemented with cookie or session instead
    # def setLang(self, lang:str="EN"): # "TH" || "EN"
    #     if (lang != "EN" or lang != "TH"):
    #         self.fname = "EN"
    #     self.langPref = lang

    # @property
    # def getLangPref(self):
    #     return self.langPref


class Game(db.Model):
    """ Database table: game
        each time that player plays game the information and result properties defined here
        """
    id = db.Column(db.Integer(), primary_key=True)
    start_time = db.Column(db.DateTime())
    finish_time = db.Column(db.DateTime())
    score = db.Column(db.Integer(), nullable=False, default=0)
    counter = db.Column(db.Integer(), nullable=False, default=0)
    played_by = db.Column(db.String(), db.ForeignKey(
        'user.fname'), nullable=False, default="Guest")

    def __str__(self) -> str:
        return str("ID: " + self.id + " Finished at: " + self.finish_time)

    def __init__(self, finish_at: datetime.datetime, score: int, played_by, start_at: datetime.datetime = None):
        def increment() -> int:  # increment doesn't work, need to be fixed
            current = self.counter
            if current == None:
                current = 0
            increased = current + 1
            self.counter = increased
            return self.counter
        self.start_time = start_at
        self.finish_time = finish_at
        self.score = score
        self.counter = increment()
        self.played_by = played_by

# class Question(db.Model):
#     """ Database table: question
#         each question that will ask users
#         """
#     q_id = db.Column(db.Integer(), nullable=False, primary_key=True) # question id
#     q = db.Column(db.String(), nullable=False) # question
#     a = db.Column(db.String(), nullable=True) # answer
