# Root file of the system
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import PendingRollbackError, OperationalError
from flask_bcrypt import Bcrypt, generate_password_hash
from flask_login import LoginManager, current_user
from flask import Flask, Blueprint, render_template, abort, flash, session
from decouple import config as en_var  # import the environment var
from datetime import timedelta
db = SQLAlchemy()
DB_NAME = en_var(
    'DATABASE_URL', "sqlite:///christmas_app2022_database.sqlite")
TIMEOUT = timedelta(hours=1)
try:
    PORT = en_var("port")
except:
    PORT = 5500

try:
    DOMAIN = en_var('server')
except:
    DOMAIN = f"christmas2022.lukecreated.com:{PORT}"


def create_app():
    app = Flask(__name__)
    f_bcrypt = Bcrypt()
    app.config['FLASK_ADMIN-SWATCH'] = 'cerulean'
    # Encrepted with Environment Variable
    app.config['SECRET_KEY'] = en_var('christmas_app2022')
    app.config['DATABASE_NAME'] = DB_NAME
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['REMEMBER_COOKIE_SECURE'] = True
    # set session timeout (need to use with before_request() below)
    app.config['PERMANENT_SESSION_LIFETIME'] = TIMEOUT
    # app.config['']
    app.config['TIMEZONE'] = 'Asia/Bangkok'
    # app.config['SERVER_NAME'] = DOMAIN

    f_bcrypt.init_app(app)
    db.init_app(app)

    from .views import views
    from .authen import auth
    from .features import features
    from .accountMng import account
    from .game import game
    from ._ss_ import acc_security
    from .customizedView import cusViews
    app.register_blueprint(rootView, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(features, url_prefix='/')
    app.register_blueprint(account, url_prefix='/')
    app.register_blueprint(game, url_prefix='/')
    app.register_blueprint(acc_security, url_prefix='/@system-@security-check')
    app.register_blueprint(cusViews, url_prefix='/')

    # with app.app_context(): # Drop all of the tables
    #     db.drop_all()

    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        db.session.rollback()
        flash(f'{e}', category='error')

    from .models import User

    # @app.before_request
    # def acc():

    #     try:
    #         d1 = User(fname="ADMIN", alias="admin",
    #                   password=generate_password_hash("admin").decode('utf-8'))
    #         db.session.add(d1)
    #         db.session.commit()
    #         try:
    #             from .accounts import create_accounts
    #             a = create_accounts()
    #             db.session.add_all(a)
    #             db.session.commit()

    #         except Exception as e:
    #             db.session.rollback()
    #             flash(f'{e}', category='error')

    #     except OperationalError:
    #         with app.app_context():
    #             db.create_all()

    #     except Exception as e:
    #         db.session.rollback()
    #         flash(f'{e}', category='error')

    # config the user session
    @app.before_request
    def before_request():
        session.permanent = True
        # session.modified = True # default set to true. Consult the lib to confirm

    login_manager = LoginManager()
    login_manager.login_view = 'auth.logIn'
    login_manager.refresh_view = 'auth.logIn'
    login_manager.login_message_category = 'info'
    login_manager.needs_refresh_message_category = "info"
    login_manager.needs_refresh_message = "You have to login again to confirm your identity!"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


class About():
    version = float()
    status = str()
    build = int()
    version_note = str()

    def __init__(self, version: float = float(0.0), status: str = 'None Stated', build: int = 20221100, version_note: str = "None Stated"):
        self.version = version
        self.status = status
        self.build = build
        self.version_note = version_note

    def __str__(self) -> str:
        return str("{ " + f"Version: {self.version} | Status: {self.status} | Build: {self.build} | Updates: {self.version_note}" + " }")

    def getSystemVersion(self) -> str:
        return str(self.version)


systemInfoObject = About(version=2.2, status='Public Release',
                         build=20230512, version_note='deploy on Render')
systemInfo = systemInfoObject.__str__()
systemVersion = systemInfoObject.getSystemVersion()

rootView = Blueprint('rootView', __name__)


@rootView.route("/root-template-view/")
def root_view():
    if not current_user.is_authenticated:
        abort(401)  # unauthorized
    elif current_user.isMe == True:
        return render_template("root.html", user=current_user)
    else:
        abort(403)  # forbidden
