# Form implementation generated from reading ui file 'D:\KTLT_NGUYENVONHUNGOC_EXERCISE\MODULE3\Exercise64\ui\MainWindow64.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 435)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 611, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(170, 85, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 311, 231))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEditId = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditId.setGeometry(QtCore.QRect(130, 30, 171, 20))
        self.lineEditId.setObjectName("lineEditId")
        self.lineEditName = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditName.setGeometry(QtCore.QRect(130, 60, 171, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditIdCard = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditIdCard.setGeometry(QtCore.QRect(130, 90, 171, 20))
        self.lineEditIdCard.setObjectName("lineEditIdCard")
        self.lineEditBirthday = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEditBirthday.setGeometry(QtCore.QRect(130, 120, 171, 20))
        self.lineEditBirthday.setObjectName("lineEditBirthday")
        self.checkBoxOfficial = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBoxOfficial.setGeometry(QtCore.QRect(130, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxOfficial.setFont(font)
        self.checkBoxOfficial.setChecked(True)
        self.checkBoxOfficial.setObjectName("checkBoxOfficial")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonSave.setGeometry(QtCore.QRect(130, 190, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonRemove = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButtonRemove.setGeometry(QtCore.QRect(210, 190, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonRemove.setFont(font)
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 60, 291, 321))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 275, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayoutButton = QtWidgets.QVBoxLayout()
        self.verticalLayoutButton.setObjectName("verticalLayoutButton")
        self.verticalLayout_2.addLayout(self.verticalLayoutButton)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 300, 311, 81))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButtonSearchIdCard = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSearchIdCard.setGeometry(QtCore.QRect(10, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSearchIdCard.setFont(font)
        self.pushButtonSearchIdCard.setObjectName("pushButtonSearchIdCard")
        self.pushButtonFilterYearofBirthday = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonFilterYearofBirthday.setGeometry(QtCore.QRect(130, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonFilterYearofBirthday.setFont(font)
        self.pushButtonFilterYearofBirthday.setObjectName("pushButtonFilterYearofBirthday")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 18))
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
        self.label.setText(_translate("MainWindow", "Employee Managements"))
        self.groupBox.setTitle(_translate("MainWindow", "Employee Details:"))
        self.label_2.setText(_translate("MainWindow", "Id:"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "ID Card:"))
        self.label_5.setText(_translate("MainWindow", "Birthday:"))
        self.checkBoxOfficial.setText(_translate("MainWindow", "Official"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Employees:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "More functions:"))
        self.pushButtonSearchIdCard.setText(_translate("MainWindow", "Search ID Card"))
        self.pushButtonFilterYearofBirthday.setText(_translate("MainWindow", "Filter Year of Birthday"))
