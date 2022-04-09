from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from modules.help import Get_info_byID, CreateFile
from modules.del_Form import DelForm
from modules.add_From import FormAdd
from modules.pows import tryParseInt
from cryptography.fernet import Fernet



class MainWindow(QMainWindow):
    """ Класс графического интерфейса для основной формы """

    def __init__(self) -> None:
        """ Иницаилизация """
        super(MainWindow, self).__init__()
        loadUi('ui_files\Check.ui', self)
        self.delform = DelForm(self)
        self.addform = FormAdd(self)
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
        self.cipherBtn.clicked.connect(self.Cipher)

    def Cipher(self):
        CreateFile()

        key = Fernet.generate_key()
        with open('sqLite/filekey.key', 'wb') as filekey:
            filekey.write(key)

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open('sqLite/foo.txt', 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open('sqLite/foo2.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        self.ShowError('Created!')

    def goto_del(self):
        self.delform.show()
        self.hide()

    def goto_add(self):
        self.addform.show()
        self.close()


    def GenerateCheck(self):
        id, f = tryParseInt(self.get_idx.toPlainText())
        if f:
            req, cost, amount, name_prod = Get_info_byID(id)
            try:
                tmp = req[0]
                a = f'Дата: {req[0]}\nФИО продавца: {req[3]}\nМагазин: {req[2]}\nНазвание продукта    Цена    Количество\n\n'
                t = {}
                for i in range(len(name_prod)):
                    t[name_prod[i]] = cost[i], amount[i]

                for key in t:
                    a += str(f'{key}:    {t[key][0]} руб.    {t[key][1]} шт.\n\n')

                a += f'\n\n\t\tИТОГО: {req[1]} руб'
                self.CheckOutput.setPlainText(a)
            except Exception:
                self.ShowError('Данного индекса не существует!')
                
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