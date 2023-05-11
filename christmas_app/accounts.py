""" Used to pre-defined user accounts """
from flask import flash
from flask_bcrypt import generate_password_hash
from .models import User
from decouple import config as en_var # import the environment var

usernames = {en_var('name_dad'):en_var('pass_dad'),en_var('name_mom'):en_var('pass_mom'),en_var('name_pa'):en_var('pass_pa'),en_var('name_mama'):en_var('pass_mama'),en_var('name_self'):en_var('pass_self') \
    ,"ADMIN":"admin"\
       ,en_var("name_papa"):en_var("pass_papa"), en_var("name_kwan"):en_var("pass_kwan"), en_var("name_wish"):en_var("pass_wish"), en_var("name_anna"):en_var('pass_anna'),en_var("name_ajT"):en_var("pass_ajT"),en_var('name_ajJ'):en_var("pass_ajJ") \
        ,en_var("name_candice"):en_var("pass_candice"), en_var("name_addy"):en_var("pass_addy"), en_var("name_evander"):en_var("pass_evander"), en_var("name_noemi"):en_var("pass_noemi"), en_var("name_grandma"):en_var("pass_grandma")}

def create_dad():
    dad = None
    try:
        dad = User(fname=en_var('name_dad'),password=generate_password_hash(usernames[en_var('name_dad')]).decode('utf-8'), alias='Dad')
    except:
        flash("Couldn't add more row to database", category='danger')
    return dad

def create_mom():
    mom = None
    try:
        mom = User(fname=en_var('name_mom'),password=generate_password_hash(usernames[en_var('name_mom')]).decode('utf-8'), alias='Mom')
    except:
        flash("Couldn't add more row to database", category='danger')
    return mom

def create_pa():
    pa = None
    try:
        pa = User(fname=en_var('name_pa'),password=generate_password_hash(usernames[en_var('name_pa')]).decode('utf-8'), alias='Pa')
    except:
        flash("Couldn't add more row to database", category='danger')
    return pa

def create_mama():
    mama = None
    try:
        mama = User(fname=en_var('name_mama'),password=generate_password_hash(usernames[en_var('name_mama')]).decode('utf-8'), alias='Mama')
    except:
        flash("Couldn't add more row to database", category='danger')
    return mama

def create_me():
    me = None
    try:
        me = User(fname=en_var('name_self'),password=generate_password_hash(usernames[en_var('name_self')]).decode('utf-8'), alias='Kan')
    except:
        flash("Couldn't add more row to database", category='danger')
    return me

def create_papa():
    papa = None
    try:
        papa = User(fname=en_var('name_papa'),password=generate_password_hash(usernames[en_var('name_papa')]).decode('utf-8'), alias='Papa')
    except:
        flash("Couldn't add more row to database papa", category='danger')
    return papa

def create_grandma():
    grandma = None
    try:
        grandma = User(fname=en_var('name_grandma'),password=generate_password_hash(usernames[en_var('name_grandma')]).decode('utf-8'), alias='Grandma')
    except:
        flash("Couldn't add more row to database grandma", category='danger')
    return grandma

def create_kwan():
    kwan = None
    try:
        kwan = User(fname=en_var('name_kwan'),password=generate_password_hash(usernames[en_var('name_kwan')]).decode('utf-8'), alias='Kwan')
    except:
        flash("Couldn't add more row to database kwan", category='danger')
    return kwan

def create_wish():
    wish = None
    try:
        wish = User(fname=en_var('name_wish'),password=generate_password_hash(usernames[en_var('name_wish')]).decode('utf-8'), alias='Wish')
    except:
        flash("Couldn't add more row to database wish", category='danger')
    return wish

def create_anna():
    anna = None
    try:
        anna = User(fname=en_var('name_anna'),password=generate_password_hash(usernames[en_var('name_anna')]).decode('utf-8'), alias='Anna')
    except:
        flash("Couldn't add more row to database anna", category='danger')
    return anna

def create_ajT():
    ajT = None
    try:
        ajT = User(fname=en_var('name_ajT'),password=generate_password_hash(usernames[en_var('name_ajT')]).decode('utf-8'), alias='AjTrithep')
    except:
        flash("Couldn't add more row to database ajt", category='danger')
    return ajT

def create_ajJ():
    ajJ = None
    try:
        ajJ = User(fname=en_var('name_ajJ'),password=generate_password_hash(usernames[en_var('name_ajJ')]).decode('utf-8'), alias='AjJade')
    except:
        flash("Couldn't add more row to database ajj", category='danger')
    return ajJ

def create_candice():
    candice = None
    try:
        candice = User(fname=en_var('name_candice'),password=generate_password_hash(usernames[en_var('name_candice')]).decode('utf-8'), alias='Candice')
    except:
        flash("Couldn't add more row to database candice", category='danger')
    return candice

def create_addy():
    addy = None
    try:
        addy = User(fname=en_var('name_addy'),password=generate_password_hash(usernames[en_var('name_addy')]).decode('utf-8'), alias='Addy')
    except:
        flash("Couldn't add more row to database addy", category='danger')
    return addy

def create_evander():
    evander = None
    try:
        evander = User(fname=en_var('name_evander'),password=generate_password_hash(usernames[en_var('name_evander')]).decode('utf-8'), alias='Evander')
    except:
        flash("Couldn't add more row to database evander", category='danger')
    return evander

def create_noemi():
    noemi = None
    try:
        noemi = User(fname=en_var('name_noemi'),password=generate_password_hash(usernames[en_var('name_noemi')]).decode('utf-8'), alias='Noemi')
    except:
        flash("Couldn't add more row to database noemi", category='danger')
    return noemi

def create_accounts():
    pa = create_pa()
    ma = create_mama()
    dad = create_dad()
    mom = create_mom()
    me = create_me()
    papa = create_papa()
    grandma = create_grandma()
    kwan = create_kwan()
    wish = create_wish()
    anna = create_anna()
    ajT = create_ajT()
    ajJ = create_ajJ()
    candice = create_candice()
    addy = create_addy()
    evander = create_evander()
    noemi = create_noemi()
    return [me, pa, ma, dad, mom, papa, grandma, kwan, wish, anna, ajJ, ajT, candice, addy, evander, noemi]