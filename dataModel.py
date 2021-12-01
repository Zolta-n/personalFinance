
import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from __init__ import app

basedir = os.path.abspath(os.path.dirname(__file__))

#pp = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
Migrate(app,db)

# Here we can start with the table definitions #

class Accounts(db.Model):

    __tablename__ = 'accounts'

    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.Text)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    account_type = db.Column(db.Text)
    is_active = db.Column(db.Boolean)
    credit_limit = db.Column(db.Float)
    balance = db.relationship('Balance', backref='accounts')
    currency = db.relationship('Currency',back_populates='accounts',uselist=False)

    def __init__(self,name,
                 currency_id, account_type='debit',
                 is_active = True, credit_limit=0):
        self.name = name
        self.currency_id = currency_id
        self.account_type = account_type
        self.is_active = is_active
        self.credit_limit = credit_limit

    def __repr__(self):

        return f'This is the {self.name} account in {self.currency.name}'




class Balance(db.Model):

    __tablename__='balance'

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer,db.ForeignKey('accounts.id'))
    day = db.Column(db.DateTime)
    value = db.Column(db.Float)

    def __init__(self, account_id, day, value):
        self.account_id = account_id
        self.day = day
        self.value = value

    def __repr__(self):
        return f'The current balance on{self.day} is {self.value} {self.accounts.currency.name}'




class Currency(db.Model):

    __tablename__='currency'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(3),primary_key=True)
    exchange_huf = db.Column(db.Float)
    accounts = db.relationship('Accounts', back_populates='currency')

    def __init__(self,name, exchange_rate):
        self.name = name
        self.exchange_huf = exchange_rate

    def __repr__(self):
        return f'Currency is {self.name}, the exchange rate to HUF is {self.exchange_huf} HUF/{self.name}'


