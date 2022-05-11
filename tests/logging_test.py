from pathlib import Path
import os

root = os.path.dirname(os.path.abspath(__file__))

def test_errorlog():
    errorLog = os.path.join(root, '../logs/errors.log')
    assert os.path.exists(errorLog) == True


def test_myapplog():
    myappLog = os.path.join(root, '../logs/myapp.log')
    assert os.path.exists(myappLog) == True


def test_requestlog():
    requestLog = os.path.join(root, '../logs/request.log')
    assert os.path.exists(requestLog) == True


def test_sqlalchemylog():
    sqlalchemyLog = os.path.join(root, '../logs/sqlalchemy.log')
    assert os.path.exists(sqlalchemyLog) == True


def test_flasklog():
    root = os.path.dirname(os.path.abspath(__file__))
    flasklog = os.path.join(root, '../logs/flask.log')
    if not os.path.exists(flasklog):
        os.mknod(flasklog)
    assert os.path.exists(flasklog) == True


def test_werkzeuglog():
    werkzeugLog = os.path.join(root, '../logs/werkzeug.log')
    assert os.path.exists(werkzeugLog) == True


def test_debuglog():
    root = os.path.dirname(os.path.abspath(__file__))
    debuglog = os.path.join(root, '../logs/debug.log')
    if not os.path.exists(debuglog):
        os.mknod(debuglog)
    assert os.path.exists(debuglog) == True

def test_upload_csvlog():
    root = os.path.dirname(os.path.abspath(__file__))
    myappLog = os.path.join(root, '../logs/uploadcsv.log')
    if not os.path.exists(myappLog):
        os.mknod(myappLog)
    assert os.path.exists(myappLog) == True



