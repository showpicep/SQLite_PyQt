import sys
sys.path.insert(0, 'C:\\Users\\Acer\\Desktop\\Chek')

from PyQt5.QtWidgets import QMainWindow, QWidget, QDesktopWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from modules.help import Get_info_byID, DelCheck
from modules.pows import tryParseInt


class DelForm(QWidget):
    """ Класс графического интерфейса для основной формы """

    def __init__(self, parent) -> None:
        """ Иницаилизация """
        super(DelForm, self).__init__()
        self.parent = parent
        loadUi('ui_files\delForm.ui', self)
        self.add_functions_for_buttons()
        self.setFixedSize(1000, 710)
        self.setWindowTitle('Remove')
        self.center()

    def add_functions_for_buttons(self) -> None:
        """ Метод для добавления функций для кнопок """
        self.backtoprev.clicked.connect(self.backtomenu)
        self.checkButt.clicked.connect(self.preview)
        self.remButt.clicked.connect(self.DelByID)

    def DelByID(self):
        id, f = tryParseInt(self.idxInput.toPlainText())
        if f:
            DelCheck(id)
        else:
            self.ShowError('Что-то не так с индексом')

    def preview(self):
        id, f = tryParseInt(self.idxInput.toPlainText())
        if f:
            req, cost, amount, name_prod = Get_info_byID(id)
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            str1 = ', '.join(name_prod)
            try:
                tmp = req[0]
                self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(req[0]))
                self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(req[2]))
                self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(req[3]))
                self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str1))
                self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(req[1])))
                # print(req[1], 'TYT', id, req, cost, amount, name_prod)
            except Exception:
                self.ShowError('Данного индекса не существует!')
        else:
            self.ShowError('Вы не ввели индекс')


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
        msg.setIcon(QMessageBox.Critical)
        msg.setText(errorText)
        msg.setWindowTitle("Attantion")
        msg.exec_()
