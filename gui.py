from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(647, 573)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start.setGeometry(QtCore.QRect(530, 10, 101, 41))
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(420, 10, 101, 41))
        self.stop.setObjectName("stop")
        self.test = QtWidgets.QPushButton(parent=self.centralwidget)
        self.test.setGeometry(QtCore.QRect(310, 10, 101, 41))
        self.test.setObjectName("test")
        self.historia = QtWidgets.QPushButton(parent=self.centralwidget)
        self.historia.setGeometry(QtCore.QRect(200, 10, 101, 41))
        self.historia.setObjectName("historia")
        
        # Timer
        self.label_timer = QtWidgets.QLabel("00:00:00", parent=self.centralwidget)
        self.label_timer.setEnabled(True)
        self.label_timer.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.label_timer.setStyleSheet("background-color: white;")
        self.label_timer.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_timer.setObjectName("label_timer")

        self.both_pallet = QtWidgets.QLabel(parent=self.centralwidget)
        self.both_pallet.setEnabled(True)
        self.both_pallet.setGeometry(QtCore.QRect(10, 70, 171, 21))
        self.both_pallet.setStyleSheet("background-color: white;")
        self.both_pallet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.both_pallet.setObjectName("both_pallet")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 100, 171, 411))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 169, 409))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pallets_list = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.pallets_list.setEnabled(True)
        self.pallets_list.setGeometry(QtCore.QRect(0, 0, 171, 411))
        self.pallets_list.setStyleSheet("background-color: white;")
        self.pallets_list.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pallets_list.setObjectName("pallets_list")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.both_pallet_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.both_pallet_2.setEnabled(True)
        self.both_pallet_2.setGeometry(QtCore.QRect(200, 70, 431, 21))
        self.both_pallet_2.setStyleSheet("background-color: white;")
        self.both_pallet_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.both_pallet_2.setObjectName("both_pallet_2")
        self.summary = QtWidgets.QLabel(parent=self.centralwidget)
        self.summary.setEnabled(True)
        self.summary.setGeometry(QtCore.QRect(200, 190, 211, 41))
        self.summary.setStyleSheet("background-color: white;")
        self.summary.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.summary.setObjectName("summary")
        self.newest_pallet = QtWidgets.QLabel(parent=self.centralwidget)
        self.newest_pallet.setEnabled(True)
        self.newest_pallet.setGeometry(QtCore.QRect(420, 190, 211, 41))
        self.newest_pallet.setStyleSheet("background-color: white;")
        self.newest_pallet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.newest_pallet.setObjectName("newest_pallet")
        self.summary_list = QtWidgets.QLabel(parent=self.centralwidget)
        self.summary_list.setEnabled(True)
        self.summary_list.setGeometry(QtCore.QRect(200, 250, 211, 261))
        self.summary_list.setStyleSheet("background-color: white;")
        self.summary_list.setText("")
        self.summary_list.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.summary_list.setObjectName("summary_list")
        self.newest_list = QtWidgets.QLabel(parent=self.centralwidget)
        self.newest_list.setEnabled(True)
        self.newest_list.setGeometry(QtCore.QRect(420, 250, 211, 261))
        self.newest_list.setStyleSheet("background-color: white;")
        self.newest_list.setText("")
        self.newest_list.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.newest_list.setObjectName("newest_list")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 100, 431, 71))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.test.setText(_translate("MainWindow", "TEST"))
        self.historia.setText(_translate("MainWindow", "HISTORIA"))
        self.label_timer.setText(_translate("MainWindow", "Czas"))
        self.both_pallet.setText(_translate("MainWindow", "Kupione palety"))
        self.pallets_list.setText(_translate("MainWindow", "Kupione palety"))
        self.both_pallet_2.setText(_translate("MainWindow", "Szukaj"))
        self.summary.setText(_translate("MainWindow", "Podsumowanie"))
        self.newest_pallet.setText(_translate("MainWindow", "Najnowsze palety"))
