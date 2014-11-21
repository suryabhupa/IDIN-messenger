import os
basedir = os.path.abspath(os.path.dirname(__file__))


if 'DATABASE_URL' in os.environ:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
else:
    # defaults to a sqllite database named data.db
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data.db')
    print "WARNING: using default sqlite database"

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')

print SQLALCHEMY_DATABASE_URI

