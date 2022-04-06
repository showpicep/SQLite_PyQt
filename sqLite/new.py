import sqlite3 as sq
import sys
import time

from models import *


def setProduct(name: str, cost: float):
    '''Функция для добавления нового продукта'''
    if checkProduct(name):
        with db:
            Purchases.create(purchases_name=name, cost=cost)
        print('Added!')
    else:
        print('Not Added')


def setRelationship(idx_check, idx_product):
    '''Функция для добавления связей между чеком и покупкой'''
    with db:
        cur_amount, f = checkAmount(idx_check, idx_product)

        if f:
            new_amount = cur_amount+1
            query = PurchasesCheck.update(amount=new_amount).where((PurchasesCheck.id_check == idx_check)
                                                           & (PurchasesCheck.id_purchases == idx_product))
            query.execute()
        else:
            PurchasesCheck.create(id_purchases=Purchases[idx_product], id_check=Check[idx_check], amount=cur_amount)


def newCheck(shop_name='Nan', seller_name='Nan'):
    with db:
        Check.get_or_create(date=datetime.date.today(), total=0, shop_name=shop_name, seller_name=seller_name)


def createTable():
    with db:
        db.create_tables([Purchases, Check, PurchasesCheck])


def request():
    with db:
        quary = (Check
                 .select()
                 .where(Check.id == 2)
                 .join(PurchasesCheck)
                 .join(Purchases)
                 .where(Purchases.purchases_name == 'Молоко')
                 )
        for res in quary:
            print(res.date)


def checkProduct(name: str) -> bool:
    a = 0
    with db:
        quary = (Purchases
                 .select()
                 .where(Purchases.purchases_name == name)
                 )
        for res in quary:
            a = res.id
    if a != 0:
        return False
    else:
        return True


def checkAmount(idx_check, idx_product):
    is_exist = False
    a = 0
    with db:
        quary = (PurchasesCheck
                 .select()
                 .where((PurchasesCheck.id_check == idx_check) & (PurchasesCheck.id_purchases == idx_product))
                 )
        for res in quary:
            a = res.amount

    if a != 0:
        is_exist = True
    else:
        a = 1

    return a, is_exist



setRelationship(1, 3)
# with db:
# purchases = [
#     {'purchases_name': 'Печенья', 'amount': 1000, 'cost': 50.0},
#     {'purchases_name': 'Кофе', 'amount': 1000, 'cost': 350.0},
#     {'purchases_name': 'Молоко', 'amount': 1000, 'cost': 80.0},
#     {'purchases_name': 'Энергетик', 'amount': 1000, 'cost': 70.0},
#     {'purchases_name': 'Шампунь', 'amount': 500, 'cost': 160.0},
#     {'purchases_name': 'Мюсли', 'amount': 500, 'cost': 90.0},
#     {'purchases_name': 'Мука', 'amount': 500, 'cost': 65.0},
#     {'purchases_name': 'Пена для бритья', 'amount': 500, 'cost': 200.0},
#     {'purchases_name': 'Яйца', 'amount': 600, 'cost': 80.0},
#     {'purchases_name': 'Хлопья', 'amount': 640, 'cost': 85.0},
#     {'purchases_name': 'Чай', 'amount': 600, 'cost': 90.0},
#     {'purchases_name': 'Чипсы', 'amount': 700, 'cost': 100.0}
# ]# Заполнение
#
# Purchases.insert_many(purchases).execute()

