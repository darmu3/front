import sys
from functools import partial

from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.titleBtn_2.setChecked(True)

        self.ui.incomeBtn_2.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageIncome))
        self.ui.incomeBtn_1.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageIncome))
        self.ui.titleBtn_1.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageTitle))
        self.ui.titleBtn_2.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageTitle))
        self.ui.scheduleBtn_1.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageSchedule))
        self.ui.scheduleBtn_2.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageSchedule))
        self.ui.socialNetworksBtn_1.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageSocialNetwork))
        self.ui.socialNetworksBtn_2.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageSocialNetwork))
        self.ui.fileSharingBtn_1.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageFileSharing))
        self.ui.fileSharingBtn_2.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageFileSharing))
        self.ui.accountBtn_1.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageAccount))
        self.ui.accountBtn_2.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageAccount))
        self.ui.aboutUs_1.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageAboutUs))
        self.ui.aboutUs_2.clicked.connect(partial(self.ui.stackedWidget.setCurrentWidget, self.ui.pageAboutUs))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
