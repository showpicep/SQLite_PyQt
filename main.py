import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from modules.interface import MainWindow

# TODO: Добавить возможность внесения и удаление данных в БД
# TODO: Перевести содержимое БД в текстовый файл и зашифравать определенным ключом

# def application():
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     widget = QStackedWidget()
#     widget.addWidget(main_window)
#     widget.show()
#     app.exec_()
# widget = QStackedWidget()

if __name__ == '__main__':
    # application()
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main_window = MainWindow()
    main_window.show()
    app.exec_()