from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

print "step 1"
app = Flask(__name__)
print "step 2"
app.config.from_object('config')
print "step 3"
db = SQLAlchemy(app)
print "step 4"

from app import views, models
print "step 5"


