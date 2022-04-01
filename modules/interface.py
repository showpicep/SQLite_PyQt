import random
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from modules.help import GetStringOfRequest
from modules.del_Form import DelForm
from modules.add_From import FormAdd
from modules.pows import tryParseInt


class MainWindow(QMainWindow):
    """ Класс графического интерфейса для основной формы """

    def __init__(self) -> None:
        """ Иницаилизация """
        super(MainWindow, self).__init__()
        loadUi('ui_files\Check.ui', self)
        self.setWindowTitle("New Menu")
        self.add_functions_for_buttons()
        self.setFixedSize(1000, 710)
        self.CheckOutput.setReadOnly(True)
        self.center()

    def add_functions_for_buttons(self) -> None:
        """ Метод для добавления функций для кнопок """
        self.GenButt.clicked.connect(self.GenerateCheck)
        self.ClearButt.clicked.connect(self.CheckClear)
        self.gotodel.clicked.connect(self.goto_del)
        self.gotoadd.clicked.connect(self.goto_add)


    def goto_del(self):
        self.delform = DelForm(self)
        self.delform.show()
        self.hide()

    def goto_add(self):
        self.addform = FormAdd(self)
        self.addform.show()
        self.close()


    def GenerateCheck(self):
        a = GetStringOfRequest()
        d = ''
        for i in a:
            d += str(f'{i} {a[i]}\n')

        self.CheckOutput.setPlainText(d)
                
    def CheckClear(self):
        self.CheckOutput.setPlainText('')

    def ShowError(self, errorText: str) -> None:
        """Метод для отображения ошибки"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(errorText)
        msg.setWindowTitle("Attantion")
        msg.exec_()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())