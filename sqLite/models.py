from peewee import *
import datetime

db = SqliteDatabase('C:\\Users\\Acer\\Desktop\\Chek\\sqLite\\chek.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Purchases(BaseModel):
    purchases_name = CharField()
    cost = FloatField()

    class Meta:
        db_table = 'purchases'


class Check(BaseModel):
    date = DateField(default=datetime.date.today)
    total = FloatField(default=0)
    shop_name = CharField(default='Nan')
    seller_name = CharField(default='Nan')

    class Meta:
        db_table = 'checks'


class PurchasesCheck(BaseModel):
    id_purchases = ForeignKeyField(Purchases, field=Purchases.id)
    id_check = ForeignKeyField(Check, field=Check.id)
    amount = IntegerField()

    class Meta:
        primary_key = CompositeKey('id_purchases', 'id_check')
