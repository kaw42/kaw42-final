from app import db
from app.db.models import User

from flask_login import FlaskLoginClient
from app.auth.forms import *

def test_balance_calculate(application):

    application.test_client_class = FlaskLoginClient
    user = User('kaw42@njit.edu', 'test123')
    db.session.add(user)
    db.session.commit()

    assert user.email == 'kaw42@njit.edu'
    assert user.balance == 0.00 # Default balance

    user.balance += 1.23
    assert user.balance == 1.23

    user.balance -= 0.23
    assert user.balance == 1.00