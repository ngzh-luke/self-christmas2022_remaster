""" Customized function(s) used in the system"""

from datetime import datetime, timezone
from . import TIMEOUT
from flask.signals import message_flashed
from flask.globals import current_app
#from flask.signals import _signals
from flask import session
import typing as t
# my_signals = _signals

# model_saved = my_signals.signal('flashed')

    
@staticmethod
# create and update virtual session cookies. 
# the actual timeout cookies are determined by Flask and they are not affect by the virtual one below
def updateSessionTime():
    if "loginTime" in session:
        session['lastActiveTime'] = datetime.now(tz=timezone.utc)
        lastActiveTime = session['lastActiveTime']
        first = session['loginTime']
        if (first > lastActiveTime):
            updatedTime = first + TIMEOUT
        else:
            updatedTime = lastActiveTime + TIMEOUT
        session['timeoutTime'] = updatedTime