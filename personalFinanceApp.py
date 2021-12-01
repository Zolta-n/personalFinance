
from flask import render_template,url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, FieldList, SubmitField, IntegerField, DateField,FormField
from wtforms import validators
from wtforms.form import BaseForm, Form
from __init__ import app
from dataModel import Accounts
from wtforms.meta import DefaultMeta

account_names=[]


app.config['SECRET_KEY']='12345'


# def form_from_fields(fields):
#     def create_form(prefix='', **kwargs):
#         form = BaseForm(fields, prefix=prefix)
#         form.process(**kwargs)
#         return form
#     return create_form

def form_from_fields(fields):
    def create_form(prefix='', **kwargs):
        form = BaseForm(fields, prefix=prefix)
        form.process(**kwargs)
        return form

    return create_form


def get_account_info():
    accounts_db = Accounts.query.all()
    account_names = []
    currencies = []
    for account in accounts_db:
        account_names.append(account.name)
        currencies.append(account.currency.name)
    return account_names,currencies


class InputForm(FlaskForm):

    submit = SubmitField('Submit')
    date = DateField('Date')
    fieldlist = FormField(form_from_fields([(account, IntegerField(account)) for account in get_account_info()[0]]))





@ app.route('/',methods=['GET','POST'])
def index():



    form = InputForm()



    if form.validate_on_submit():
        first = form.fieldlist.data
        print(first)
        print(form.date.data)
        return redirect(url_for('report'))

    return render_template('index.html',form=form,currencies=get_account_info()[1])

@app.route('/report')
def report():
    return render_template('report.html')

def settings():
    pass

if __name__=='__main__':
    app.run(host="localhost", port=5001, debug=True)