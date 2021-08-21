from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField,FieldList, SubmitField, IntegerField,DateField
from wtforms import validators

myFields=[{'account':'HUF Account','currency':'HUF', 'type':'debit'},
            {'account':'EUR Account','currency':'EUR', 'type':'debit'},
            {'account':'Credit Card - Wizzair','currency':'HUF', 'type':'credit'},
            {'account':'ICBC Account','currency':'CNY', 'type':'debit'}]



app=Flask(__name__)


app.config['SECRET_KEY']='12345'



class InputForm(FlaskForm):

    fields = FieldList(StringField())
    submit = SubmitField('Submit')
    date= DateField('Date')

    def add_entry(self,names):


        for name in names:
            self.fields.append_entry(IntegerField(name=name, validators=[validators.DataRequired()],label=name, placeholder='0'))
            self.fields.entries[-1].data=''
            self.fields.entries[-1].label=name



@ app.route('/',methods=['GET','POST'])
def index():


    accounts = [myFields[x]['account'] for x in range(len(myFields))]
    currencies= [myFields[x]['currency'] for x in range(len(myFields))]

    form = InputForm()

    # Clean all obsolate fields if any
    entries_count=len(form.fields.entries)
    for field in range(entries_count):
        form.fields.pop_entry()

    # Add filds based on the list
    form.add_entry(accounts)



    if form.validate_on_submit():
        pass

    return render_template('index.html',form=form,currencies=currencies)

def report():
    pass

def settings():
    pass

if __name__=='__main__':
    app.run(debug=True)