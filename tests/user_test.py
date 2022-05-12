import logging

from app import db
from app.db.models import User, Transactions
from faker import Faker

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transactions).count() == 0
        #showing how to add a record
        #create a record
        user = User('kaw42@njit.edu', 'testtest')
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='kaw42@njit.edu').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'kaw42@njit.edu'
        #this is how you get a related record ready for insert
        user.transactions= [Transactions(200.0,"Debit"),Transactions(300.0,"Credit")]
        #commit is what saves the songs
        db.session.commit()
        assert db.session.query(Transactions).count() == 2
        transaction1 = Transactions.query.filter_by(account_type='Debit').first()
        assert transaction1.amount == 200.0
        db.session.commit()
        transaction2 = Transactions.query.filter_by(amount=300.0).first()
        assert transaction2.account_type == "Credit"
        #checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Transactions).count() == 0