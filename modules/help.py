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


#print(Get_info_byID(1))