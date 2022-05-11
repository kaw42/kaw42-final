from app import db
from app.auth.forms import *
from flask_login import FlaskLoginClient
from app.db.models import User


def test_login_validates(application, client):
    """ Tests successful login"""
    form = login_form()
    form.email.data = "kaw42@njit.edu"
    form.password.data = "kellywu10"
    assert form.validate()


def test_login_not_validates(application, client):
    """ Tests unsuccessful login"""
    form = login_form()
    form.email.data = "kaw42@njit.edu"
    form.password.data = "  "
    assert not form.validate()


def test_register_validates(application, client):
    """ Tests successful register """
    form = register_form()
    form.email.data = "kaw42@njit.edu"
    form.password.data = "kellywu10"
    form.confirm.data = "kellywu10"
    assert form.validate()


def test_dashboard_access_granted(application, client, add_user):
    """ Tests dashboard access """
    application.test_client_class = FlaskLoginClient
    user = User.query.get(1)
    assert db.session.query(User).count() == 1
    assert user.email == 'keith@webizly.com'
    with application.test_client(user=user) as client:
        response = client.get('/dashboard')
        assert b'keith@webizly.com' in response.data
        assert response.status_code == 200


def test_dashboard_access_denied(application, client):
    """ Tests denied access to the dashboard """
    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 0
    with application.test_client(user=None) as client:
        response = client.get('/dashboard')
        assert response.status_code != 200
        assert response.status_code == 302


def test_csv_upload_granted(application, client, add_user):
    """ Test to verify that the CSV file is uploaded and processed """
    application.test_client_class = FlaskLoginClient
    user = User.query.get(1)
    assert db.session.query(User).count() == 1
    assert user.email == 'keith@webizly.com'
    with application.test_client(user=user) as client:
        response = client.get('/songs/upload')
        assert response.status_code == 200
