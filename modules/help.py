import datetime
import sys

sys.path.insert(0, 'C:\\Users\\Acer\\Desktop\\Chek')
# print(sys.path)
from sqLite import models


def Get_info_byID(idx: int):
    req = []

    with models.db:
        # Получаем инфу описанную в чеке
        cost, amount, name_prod = Set_total_forCheck(idx)

        quary = (models.Check
                 .select()
                 .where(models.Check.id == idx)
                 )
        for res in quary:
            req.append(str(res.date))
            req.append(res.total)
            req.append(res.shop_name)
            req.append(res.seller_name)

        return req, cost, amount, name_prod


def Set_total_forCheck(idx: int):
    cost = []
    amount = []
    name_prod = []

    with models.db:
        quary = (models.Purchases
                 .select()
                 .join(models.PurchasesCheck)
                 .where(models.PurchasesCheck.id_check == idx)
                 )
        for res in quary:
            cost.append(res.cost)
            name_prod.append(res.purchases_name)

        quary = (models.PurchasesCheck
                 .select()
                 .where(models.PurchasesCheck.id_check == idx)
                 )
        for res in quary:
            amount.append(res.amount)

        res = sum([cost[i]*amount[i] for i in range(len(cost))])
        update = models.Check.update(total=res).where(models.Check.id == idx)
        update.execute()
        return cost, amount, name_prod


# def GetidxCheck(date, shop_name, seller_name):
#     with models.db:
#         quary = (models.Check
#                  .select()
#                  .where(models.Check.date == date
#                         & models.Check.shop_name == shop_name
#                         & models.Check.seller_name == seller_name
#                         & models.Check.total == 0.0)
#                  )
#         for res in quary:
#             return res.id, res.total
#     pass


def CreateCheck(seller_name: str, shop_name: str, id_amount: dict):
    with models.db:
        tmp = models.Check(date=datetime.date.today(), total=0, shop_name=shop_name, seller_name=seller_name)
        tmp.save()
        idx = tmp.id
        for i in id_amount:  # Связь
            models.PurchasesCheck.create(id_purchases=models.Purchases[i], id_check=models.Check[idx],
                                         amount=id_amount[i])
        Set_total_forCheck(idx)


def GetLastIdCheck():
    last = -1
    with models.db:
        queru = models.Check.select()
        for res in queru:
            last = res.id
    return last


def UpdateIdCheck(old: int, new: int):
    with models.db:
        query = models.Check.update(id=new).where(models.Check.id == old)
        query.execute()


def UpdateIdCheckInRelation(old: int, new: int):
    with models.db:
        query = models.PurchasesCheck.update(id_check=new).where(models.PurchasesCheck.id_check == old)
        query.execute()


def DelCheck(idx: int):  #idx = new, old = last
    last = GetLastIdCheck()
    with models.db:
        q1 = models.PurchasesCheck.delete().where(models.PurchasesCheck.id_check == idx)
        q2 = models.Check.delete().where(models.Check.id == idx)
        q1.execute()
        q2.execute()

        UpdateIdCheck(last, idx)
        UpdateIdCheckInRelation(last, idx)


def CreateFile():
    with models.db:
        query = models.Check.select()
        q1 = models.Purchases.select()
        q2 = models.PurchasesCheck.select()
        s1 = {}
        s2 = {}
        s3 = {}
        for idx, res in enumerate(query):
            s1[idx] = [res.id, str(res.date), res.total]
        for idx, res in enumerate(q1):
            s2[idx] = [res.id, res.purchases_name, res.cost]
        for idx, res in enumerate(q2):
            s3[idx] = [str(res.id_check), str(res.id_purchases)]
        print(s1, s2, s3, sep='\n')
        open('sqLite/foo.txt', 'w').close()
        with open('sqLite/foo.txt', 'a') as fp:
            for i in s1:
                fp.write(str(i) + ' ' + str(s1[i]) + '\n')
            for i in s2:
                fp.write('\n')
                fp.write(str(i) + ' ' + str(s2[i]) + '\n')
            for i in s3:
                fp.write('\n')
                fp.write(str(i) + ' ' + str(s3[i]) + '\n')
