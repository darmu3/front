# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1128, 635)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4.addWidget(self.widget_3)

        self.openMenuBtn = QPushButton(self.widget)
        self.openMenuBtn.setObjectName(u"openMenuBtn")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/free-icon-chevron-248744.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openMenuBtn.setIcon(icon1)
        self.openMenuBtn.setIconSize(QSize(20, 20))
        self.openMenuBtn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.openMenuBtn)

        self.horizontalSpacer_3 = QSpacerItem(742, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout.addWidget(self.widget, 0, 2, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageTitle = QWidget()
        self.pageTitle.setObjectName(u"pageTitle")
        self.gridLayout_2 = QGridLayout(self.pageTitle)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.SearchEdit = QLineEdit(self.pageTitle)
        self.SearchEdit.setObjectName(u"SearchEdit")

        self.horizontalLayout_3.addWidget(self.SearchEdit)

        self.SearchBtn = QPushButton(self.pageTitle)
        self.SearchBtn.setObjectName(u"SearchBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/free-icon-magnifier-3593144.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SearchBtn.setIcon(icon2)
        self.SearchBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.SearchBtn)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.pageTitle)
        self.pageIncome = QWidget()
        self.pageIncome.setObjectName(u"pageIncome")
        self.gridLayout_3 = QGridLayout(self.pageIncome)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.pageIncome)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageIncome)
        self.pageSchedule = QWidget()
        self.pageSchedule.setObjectName(u"pageSchedule")
        self.gridLayout_4 = QGridLayout(self.pageSchedule)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.pageSchedule)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageSchedule)
        self.pageSocialNetwork = QWidget()
        self.pageSocialNetwork.setObjectName(u"pageSocialNetwork")
        self.gridLayout_5 = QGridLayout(self.pageSocialNetwork)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_6 = QLabel(self.pageSocialNetwork)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageSocialNetwork)
        self.pageFileSharing = QWidget()
        self.pageFileSharing.setObjectName(u"pageFileSharing")
        self.gridLayout_6 = QGridLayout(self.pageFileSharing)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_7 = QLabel(self.pageFileSharing)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageFileSharing)
        self.pageAccount = QWidget()
        self.pageAccount.setObjectName(u"pageAccount")
        self.gridLayout_7 = QGridLayout(self.pageAccount)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_8 = QLabel(self.pageAccount)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageAccount)
        self.pageAboutUs = QWidget()
        self.pageAboutUs.setObjectName(u"pageAboutUs")
        self.gridLayout_8 = QGridLayout(self.pageAboutUs)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_9 = QLabel(self.pageAboutUs)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_8.addWidget(self.label_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageAboutUs)

        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)

        self.fullMenu = QWidget(self.centralwidget)
        self.fullMenu.setObjectName(u"fullMenu")
        self.verticalLayout_4 = QVBoxLayout(self.fullMenu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.fullMenu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.fullMenu)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(9)
        font.setBold(False)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.titleBtn_2 = QPushButton(self.fullMenu)
        self.titleBtn_2.setObjectName(u"titleBtn_2")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/free-icon-book-9193009.png", QSize(), QIcon.Normal, QIcon.Off)
        self.titleBtn_2.setIcon(icon3)
        self.titleBtn_2.setIconSize(QSize(20, 20))
        self.titleBtn_2.setCheckable(True)
        self.titleBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.titleBtn_2)

        self.incomeBtn_2 = QPushButton(self.fullMenu)
        self.incomeBtn_2.setObjectName(u"incomeBtn_2")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/free-icon-coin-550650.png", QSize(), QIcon.Normal, QIcon.Off)
        self.incomeBtn_2.setIcon(icon4)
        self.incomeBtn_2.setIconSize(QSize(20, 20))
        self.incomeBtn_2.setCheckable(True)
        self.incomeBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.incomeBtn_2)

        self.scheduleBtn_2 = QPushButton(self.fullMenu)
        self.scheduleBtn_2.setObjectName(u"scheduleBtn_2")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/free-icon-clock-2902894.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scheduleBtn_2.setIcon(icon5)
        self.scheduleBtn_2.setIconSize(QSize(20, 20))
        self.scheduleBtn_2.setCheckable(True)
        self.scheduleBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.scheduleBtn_2)

        self.socialNetworksBtn_2 = QPushButton(self.fullMenu)
        self.socialNetworksBtn_2.setObjectName(u"socialNetworksBtn_2")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/free-icon-social-media-9351311.png", QSize(), QIcon.Normal, QIcon.Off)
        self.socialNetworksBtn_2.setIcon(icon6)
        self.socialNetworksBtn_2.setIconSize(QSize(20, 20))
        self.socialNetworksBtn_2.setCheckable(True)
        self.socialNetworksBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.socialNetworksBtn_2)

        self.fileSharingBtn_2 = QPushButton(self.fullMenu)
        self.fileSharingBtn_2.setObjectName(u"fileSharingBtn_2")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/free-icon-file-sharing-10004135.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileSharingBtn_2.setIcon(icon7)
        self.fileSharingBtn_2.setIconSize(QSize(20, 20))
        self.fileSharingBtn_2.setCheckable(True)
        self.fileSharingBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.fileSharingBtn_2)

        self.accountBtn_2 = QPushButton(self.fullMenu)
        self.accountBtn_2.setObjectName(u"accountBtn_2")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/person.png", QSize(), QIcon.Normal, QIcon.Off)
        self.accountBtn_2.setIcon(icon8)
        self.accountBtn_2.setIconSize(QSize(20, 20))
        self.accountBtn_2.setCheckable(True)
        self.accountBtn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.accountBtn_2)

        self.aboutUs_2 = QPushButton(self.fullMenu)
        self.aboutUs_2.setObjectName(u"aboutUs_2")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutUs_2.setIcon(icon9)
        self.aboutUs_2.setIconSize(QSize(20, 20))
        self.aboutUs_2.setCheckable(True)
        self.aboutUs_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.aboutUs_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 382, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.fullMenu, 0, 1, 2, 1)

        self.icon = QWidget(self.centralwidget)
        self.icon.setObjectName(u"icon")
        self.verticalLayout_3 = QVBoxLayout(self.icon)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.icon)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleBtn_1 = QPushButton(self.icon)
        self.titleBtn_1.setObjectName(u"titleBtn_1")
        self.titleBtn_1.setIcon(icon3)
        self.titleBtn_1.setIconSize(QSize(20, 20))
        self.titleBtn_1.setCheckable(True)
        self.titleBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.titleBtn_1)

        self.incomeBtn_1 = QPushButton(self.icon)
        self.incomeBtn_1.setObjectName(u"incomeBtn_1")
        self.incomeBtn_1.setIcon(icon4)
        self.incomeBtn_1.setIconSize(QSize(20, 20))
        self.incomeBtn_1.setCheckable(True)
        self.incomeBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.incomeBtn_1)

        self.scheduleBtn_1 = QPushButton(self.icon)
        self.scheduleBtn_1.setObjectName(u"scheduleBtn_1")
        self.scheduleBtn_1.setIcon(icon5)
        self.scheduleBtn_1.setIconSize(QSize(20, 20))
        self.scheduleBtn_1.setCheckable(True)
        self.scheduleBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.scheduleBtn_1)

        self.socialNetworksBtn_1 = QPushButton(self.icon)
        self.socialNetworksBtn_1.setObjectName(u"socialNetworksBtn_1")
        self.socialNetworksBtn_1.setIcon(icon6)
        self.socialNetworksBtn_1.setIconSize(QSize(20, 20))
        self.socialNetworksBtn_1.setCheckable(True)
        self.socialNetworksBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.socialNetworksBtn_1)

        self.fileSharingBtn_1 = QPushButton(self.icon)
        self.fileSharingBtn_1.setObjectName(u"fileSharingBtn_1")
        self.fileSharingBtn_1.setIcon(icon7)
        self.fileSharingBtn_1.setIconSize(QSize(20, 20))
        self.fileSharingBtn_1.setCheckable(True)
        self.fileSharingBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.fileSharingBtn_1)

        self.accountBtn_1 = QPushButton(self.icon)
        self.accountBtn_1.setObjectName(u"accountBtn_1")
        self.accountBtn_1.setIcon(icon8)
        self.accountBtn_1.setIconSize(QSize(20, 20))
        self.accountBtn_1.setCheckable(True)
        self.accountBtn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.accountBtn_1)

        self.aboutUs_1 = QPushButton(self.icon)
        self.aboutUs_1.setObjectName(u"aboutUs_1")
        self.aboutUs_1.setIcon(icon9)
        self.aboutUs_1.setIconSize(QSize(20, 20))
        self.aboutUs_1.setCheckable(True)
        self.aboutUs_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.aboutUs_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 382, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.icon, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.openMenuBtn.toggled.connect(self.icon.setVisible)
        self.openMenuBtn.toggled.connect(self.fullMenu.setHidden)
        self.titleBtn_1.toggled.connect(self.titleBtn_2.setChecked)
        self.incomeBtn_1.toggled.connect(self.incomeBtn_2.setChecked)
        self.scheduleBtn_1.toggled.connect(self.scheduleBtn_2.setChecked)
        self.socialNetworksBtn_1.toggled.connect(self.socialNetworksBtn_2.setChecked)
        self.fileSharingBtn_1.toggled.connect(self.fileSharingBtn_2.setChecked)
        self.accountBtn_1.toggled.connect(self.accountBtn_2.setChecked)
        self.aboutUs_1.toggled.connect(self.aboutUs_2.setChecked)
        self.titleBtn_2.toggled.connect(self.titleBtn_1.setChecked)
        self.incomeBtn_2.toggled.connect(self.incomeBtn_1.setChecked)
        self.scheduleBtn_2.toggled.connect(self.scheduleBtn_1.setChecked)
        self.socialNetworksBtn_2.toggled.connect(self.socialNetworksBtn_1.setChecked)
        self.fileSharingBtn_2.toggled.connect(self.fileSharingBtn_1.setChecked)
        self.accountBtn_2.toggled.connect(self.accountBtn_1.setChecked)
        self.aboutUs_2.toggled.connect(self.aboutUs_1.setChecked)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openMenuBtn.setText("")
        self.SearchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.SearchBtn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Incomel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SocialNetworks", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"FileSharing", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"AboutUs", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"DADA GROUP", None))
        self.titleBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u0442\u043b\u044b", None))
        self.incomeBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434\u044b", None))
        self.scheduleBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.socialNetworksBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0446. \u0441\u0435\u0442\u0438", None))
        self.fileSharingBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043c\u0435\u043d \u0444\u0430\u0439\u043b\u0430\u043c\u0438", None))
        self.accountBtn_2.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.aboutUs_2.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043d\u0430\u0441", None))
        self.label.setText("")
        self.titleBtn_1.setText("")
        self.incomeBtn_1.setText("")
        self.scheduleBtn_1.setText("")
        self.socialNetworksBtn_1.setText("")
        self.fileSharingBtn_1.setText("")
        self.accountBtn_1.setText("")
        self.aboutUs_1.setText("")
    # retranslateUi

