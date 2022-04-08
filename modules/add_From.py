import sys

from PyQt5 import QtCore

sys.path.insert(0, 'C:\\Users\\Acer\\Desktop\\Chek')
from modules.help import CreateCheck
from PyQt5.QtWidgets import QMainWindow, QWidget, QDesktopWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from sqLite import models as m


class FormAdd(QWidget):
    """ Класс графического интерфейса для основной формы """

    def __init__(self, parent) -> None:
        """ Иницаилизация """
        super(FormAdd, self).__init__()
        self.parent = parent
        loadUi('ui_files/addForm.ui', self)
        self.add_functions_for_buttons()
        self.setFixedSize(1000, 710)
        self.setWindowTitle('Add')
        self.center()
        self.shops_sallers_name = {}
        self.setupNames()

    def freezCol(self, txt):
        tmp = QTableWidgetItem()
        tmp.setText(str(txt))
        tmp.setFlags(QtCore.Qt.ItemIsEnabled)
        return tmp

    def setupNames(self):
        names = []
        cost = []
        with m.db:
            query = m.Purchases.select()
            for res in query:
                names.append(res.purchases_name)
                cost.append(res.cost)
        for i in range(len(names)):
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(self.freezCol(names[i])))
            self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(self.freezCol(cost[i])))
            self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(0)))

        self.shops_sallers_name = {'Пятерочка': ['Блохина Екатерина Юрьевна', 'Павлов Фёдор Демьянович', 'Филиппова Аделина Матвеевна'],
                            'Магнит': ['Лыкова Александра Арсентьевна', 'Филиппова София Владимировна', 'Жуков Серафим Денисович'],
                            'Эдельвейс': ['Тихонов Илья Даниилович', 'Павлов Александр Дмитриевич', 'Васильев Михаил Львович']
                            }
        for i in self.shops_sallers_name:
            self.ShopName.addItem(i)
        self.ShopName.setCurrentText('')

    def Creation(self):
        changes = {}  # Ключ является id продукта, а значение количеством данного продукта
        for i in range(self.tableWidget.rowCount()):
            text = self.tableWidget.item(i, 2).text()
            if text != '0':
                changes[i+1] = text  #self.tableWidget.item(i, 0).text()

        if len(changes.keys()) != 0:
            CreateCheck(seller_name=self.SellerName.currentText(), shop_name=self.ShopName.currentText(),
                        id_amount=changes)
            self.ShowError('Чек создан')
        else:
            self.ShowError('Невозможно создать чек, так как вы не добавили продукты')
        print(changes)

    def add_functions_for_buttons(self) -> None:
        """ Метод для добавления функций для кнопок """
        self.backtoprev.clicked.connect(self.backtomenu)
        self.CreateButton.clicked.connect(self.Creation)
        self.ShopName.currentIndexChanged.connect(self.test1)

    def test1(self):
        self.SellerName.clear()
        for i in self.shops_sallers_name:
            if self.ShopName.currentText() == i:
                for j in self.shops_sallers_name[i]:
                    self.SellerName.addItem(j)
        #self.ShowError(str(self.ShopName.currentText()))

    def backtomenu(self):
        self.close()
        self.parent.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def ShowError(self, errorText: str) -> None:
        """Метод для отображения ошибки"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(errorText)
        msg.setWindowTitle("Attantion")
        msg.exec_()
