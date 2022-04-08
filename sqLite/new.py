import sys
sys.path.insert(0, 'C:\\Users\\Acer\\Desktop\\Chek\\sqLite')
#print('\n\n', sys.path)
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



