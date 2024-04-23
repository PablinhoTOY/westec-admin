from functools import wraps
import platform
import os
import time
import logging
from flask import Flask, request
from app.config import config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from logging.config import dictConfig
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

from flask_babel import Babel

os.environ['TZ'] = 'America/Bogota'
try: time.tzset()
except: pass

def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# -----------------------------Sección para cargar archivo .env-------------------------------
# -----------------------------------------------------------------------

# refers to application_top
APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)

app = Flask(__name__)
enviroment = config["development"]
app.config.from_object(enviroment)
babel = Babel(app, locale_selector=get_locale)
db = SQLAlchemy(app)

Migrate(app, db)
CORS(app, supports_credentials=True)


@app.context_processor
def inject_now():
   return {'now': datetime.date.today()}

app.config["SECURITY_TRACKABLE"] = True
app.config["SECRET_KEY"] = os.getenv("SKEY")

# If true this will only allow the cookies that contain your JWTs to be sent
# over https. In production, this should always be set to True

app.config["JWT_COOKIE_SECURE"] = True
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_SECRET_KEY"] = os.getenv("SKEY")  # Change this in your code!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

# -----------------------------------------------------------------------
# -----------------------------Bitácora-------------------------------
# -----------------------------------------------------------------------

baseDir = os.path.abspath(os.path.dirname(__file__))
month = datetime.now().strftime("%B")
year = datetime.now().strftime("%Y")

if platform.system() == "Windows":
    path = os.path.join(baseDir, "logs\\{}\\{}".format(year, month))
else:
    path = os.path.join(baseDir, "logs/{}/{}".format(year, month))

isExist = os.path.exists(path)
if not isExist:
    # Create a new directory if it doesn't exist
    os.makedirs(path)

logname = os.path.join(path, "bitacora.json".format(year, month))

LOGGING_CONFIG = { 
    
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s | %(module)s] %(message)s",
                "datefmt": "%B %d, %Y %H:%M:%S %Z",
            },
            'simple': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                "datefmt": "%B %d, %Y %H:%M:%S %Z",
        },
            'detailed': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s:%(lineno)d',
                "datefmt": "%B %d, %Y %H:%M:%S %Z",
        },
            "json": {
                "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
                    "format": "%(asctime)s %(levelname)s %(message)s - %(pathname)s:%(lineno)d",
                    "datefmt": "%B %d, %Y %H:%M:%S",

            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                'level': 'DEBUG',
                "formatter": 'detailed',
                'stream': 'ext://sys.stdout',
            },
            "file-handler": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": logname,
                "when": "midnight",
                "formatter": 'simple',
            },
            "file-handler-json": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": logname,
                "when": "midnight",
                "formatter": "json",
            },
        },
        "root": {"level": "INFO", "handlers": ["console"]},
        
        "loggers": {
            "modulos": {
                "level": "INFO",
                "handlers": ["file-handler-json"],
                "propagate": False,
            }
        },
    }

logging.config.dictConfig(LOGGING_CONFIG)



if platform.system() == "Windows":
     UPLOAD_FOLDER = os.path.join(baseDir, "static\\files\\documentacion\\{}\\{}".format(year, month))
else:
    UPLOAD_FOLDER = os.path.join(baseDir, "static/files/documentacion/{}/{}".format(year, month))
    
isExistUpload = os.path.exists(UPLOAD_FOLDER)
if not isExistUpload:
    # Create a new directory because it does not exist
     os.makedirs(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'pdf', 'jpeg', 'jpg', 'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


# -----------------------------------------------------------------------
# -----------------------------Datos del Correo-------------------------------
# -----------------------------------------------------------------------
# CONFIG EMAIL
app.config["MAIL_SERVER"] = "sandbox.smtp.mailtrap.io"
app.config["MAIL_PORT"] = 2525
app.config["MAIL_USERNAME"] = "fea2744adb3e00"
app.config["MAIL_PASSWORD"] = "cabfb7d360e07f"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_DEFAULT_SENDER"] = '"Westec  dev" <nicpanama@utp.ac.pa>'
app.config["MAIL_DEBUG"] = False

mail = Mail(app)

@app.cli.command()
def seed():
        """Add seed data to the database."""
        from seed_inicial import seed_db
        seed_db()

from app.routes import *

from app.modules.users.views import users

# blueprints
app.register_blueprint(users)
