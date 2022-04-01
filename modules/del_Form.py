from PyQt5.QtWidgets import QMainWindow, QWidget, QDesktopWidget
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from modules.help import GetStringOfRequest

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

    def backtomenu(self):
        self.close()
        self.parent.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
