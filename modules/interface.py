import random
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from modules.help import GetStringOfRequest
from modules.pows import tryParseInt


class UIWindow(QMainWindow):
    """ Класс графического интерфейса для основной формы """

    def __init__(self) -> None:
        """ Иницаилизация """
        super(UIWindow, self).__init__()
        loadUi('ui_files\Check.ui', self)
        self.add_functions_for_buttons()
        self.setFixedSize(1000, 710)
        self.CheckOutput.setReadOnly(True)

    def add_functions_for_buttons(self) -> None:
        """ Метод для добавления функций для кнопок """
        self.GenButt.clicked.connect(self.GenerateCheck)
        self.ClearButt.clicked.connect(self.CheckClear)

    def GenerateCheck(self):
        a = GetStringOfRequest()
        d = ''
        for i in a:
            d += str(f'{i} {a[i]}\n')

        self.CheckOutput.setPlainText(d)
                
    def CheckClear(self):
        self.CheckOutput.setPlainText('')

    def ShowError(self, errorText: str) -> None:
        """Метод для отображения ошибки
        """
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(errorText)
        msg.setWindowTitle("Attantion")
        msg.exec_()


    # def CheckNumPrime(self):
    #     """ Метод для проверки числа на простоту"""
    #     cur,flag = tryParseInt(self.GetCheckedValue.toPlainText())
    #     test_count = 20
    #     if flag:
    #         if is_prime(cur,test_count):
    #             self.OutputResult.setPlainText(f'С веротяностью в {1-(1/2)**test_count} данное число простое')
    #         else:
    #             self.OutputResult.setPlainText(f'С веротяностью в {1-(1/2)**test_count} данное число не простое')
    #     else:
    #         self.ShowError('Вы не ввели число для проверки!')

    # def GenerateNum(self):
    #     """ Метод для генерации простого числа"""
    #     numBits,flag = tryParseInt(self.NumOfBits.toPlainText())
    #     test_count = 10

    #     if flag:
    #         cur = nBitRandom(numBits)
    #         while(not is_prime(cur,test_count)):
    #             cur = nBitRandom(numBits)

    #         self.textEdit.setPlainText(f'С веротяностью в {1-(1/2)**test_count} данное число простое:\n' + str(cur))
    #     else:
    #         self.ShowError('Некорректный ввод кол-ва битов!')