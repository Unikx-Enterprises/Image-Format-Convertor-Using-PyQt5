# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iec_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(801, 651)
        self.horizontalFrame = QtWidgets.QFrame(Dialog)
        self.horizontalFrame.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.gridFrame = QtWidgets.QFrame(Dialog)
        self.gridFrame.setGeometry(QtCore.QRect(0, 480, 461, 141))
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridFrame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridFrame)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridFrame)
        self.comboBox.setEnabled(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridFrame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridFrame)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridFrame)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 3, 1, 1)
        self.verticalFrame = QtWidgets.QFrame(Dialog)
        self.verticalFrame.setGeometry(QtCore.QRect(470, 50, 331, 511))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalFrame)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("no_image.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.formFrame = QtWidgets.QFrame(self.verticalFrame)
        self.formFrame.setEnabled(True)
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.formFrame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.label_5 = QtWidgets.QLabel(self.formFrame)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.label_6 = QtWidgets.QLabel(self.formFrame)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.label_7 = QtWidgets.QLabel(self.formFrame)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.SpanningRole, spacerItem3)
        self.label_8 = QtWidgets.QLabel(self.formFrame)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_7.setEnabled(True)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.verticalLayout.addWidget(self.formFrame)
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setGeometry(QtCore.QRect(470, 570, 331, 51))
        self.pushButton_10.setObjectName("pushButton_10")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(0, 630, 801, 21))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(0, 50, 471, 451))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Unikx Image Convertor"))
        self.pushButton_3.setText(_translate("Dialog", "Add File"))
        self.pushButton_8.setText(_translate("Dialog", "Add Folder"))
        self.pushButton_7.setText(_translate("Dialog", "Remove All"))
        self.pushButton_6.setText(_translate("Dialog", "Select All"))
        self.pushButton_5.setText(_translate("Dialog", "Edit File"))
        self.pushButton_4.setText(_translate("Dialog", "Help"))
        self.label_2.setText(_translate("Dialog", "Output Folder:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Select Or Type Output Folder Path...."))
        self.comboBox.setItemText(0, _translate("Dialog", "png"))
        self.comboBox.setItemText(1, _translate("Dialog", "jpeg"))
        self.comboBox.setItemText(2, _translate("Dialog", "jpg"))
        self.comboBox.setItemText(3, _translate("Dialog", "gif"))
        self.comboBox.setItemText(4, _translate("Dialog", "ico"))
        self.label.setText(_translate("Dialog", "Output Format:"))
        self.pushButton_9.setText(_translate("Dialog", "Current"))
        self.pushButton_11.setText(_translate("Dialog", "Browse"))
        self.label_4.setText(_translate("Dialog", " Name :"))
        self.label_5.setText(_translate("Dialog", " Format :"))
        self.label_6.setText(_translate("Dialog", " Size :"))
        self.label_7.setText(_translate("Dialog", " Folder :"))
        self.label_8.setText(_translate("Dialog", " Dimension :"))
        self.pushButton_10.setText(_translate("Dialog", "Convert"))