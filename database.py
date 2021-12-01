from dataModel import Accounts,Currency,Balance

huf = Currency('HUF',1)
eur = Currency('EUR', 369.33)
cny = Currency('CNY',51.04)

# cur = Currency.query.filter_by(name='CNY').first()
# cnbc = Accounts('CNBC',cur.id,'debit',True,0)

# account=Accounts.query.filter_by(name='CNBC').first()
#
# balance=Balance(account.id,datetime.now(),2.0)
#
# db.session.add_all([balance])
# db.session.commit()



# db.session.query(Accounts).delete()
# db.session.query(Balance).delete()
# db.session.commit()

a=Accounts.query.all()
c=Currency.query.all()
b=Balance.query.all()
account_names=[]
for account in a:
    account_names.append(account.name)
print(a)
print(account_names)
print(b)


