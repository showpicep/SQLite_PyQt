import sys
from PyQt5.QtWidgets import QApplication
from modules.interface import UIWindow

# TODO: Добавить возможность внесения и удаление данных в БД
# TODO: Перевести содержимое БД в текстовый файл и зашифравать определенным ключом
# TODO: Добавить возможность показа определнногой чека (например по id)

def application():
    app = QApplication(sys.argv)
    main_window = UIWindow()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    application()
