from PyQt5 import QtCore, QtGui, QtWidgets
from MathMines.MathMines.questions.verifyQuestion import verifyQuestion as vq
from MathMines.MathMines import label
import random


class Ui_MathMines(object):
    def setupUi(self, MathMines):
        MathMines.setObjectName("MathMines")
        MathMines.resize(846, 428)
        self.groupBox = QtWidgets.QGroupBox(MathMines)
        self.groupBox.setGeometry(QtCore.QRect(50, 40, 301, 341))
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.groupBox.setStyleSheet(".QPushButton{\n"
                                    "background:red;\n"
                                    "color:white;\n"
                                    "border-color:black;\n"
                                    "border-style:outset;\n"
                                    "border-width:2px;\n"
                                    "border-radius:10px;\n"
                                    "border-color:black;\n"
                                    "font:bold 14px;\n"
                                    "padding: 25px 10px;\n"
                                    "min-width:6px;\n"
                                    "}\n"
                                    "\n"
                                    ".QPushButton:hover{\n"
                                    "background:blue;\n"
                                    "}\n"
                                    "")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 3, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 1, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setText("B")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 2, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setText("A")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 3, 3, 1, 1)
        self.stackedWidget_initial = QtWidgets.QStackedWidget(MathMines)
        self.stackedWidget_initial.setGeometry(QtCore.QRect(420, 10, 411, 401))
        self.stackedWidget_initial.setObjectName("stackedWidget_initial")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 371, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.stackedWidget_initial.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 401, 331))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Answer_A = QtWidgets.QPushButton(self.page_2)
        self.Answer_A.setGeometry(QtCore.QRect(30, 340, 61, 51))
        self.Answer_A.setObjectName("Answer_A")
        self.Answer_B = QtWidgets.QPushButton(self.page_2)
        self.Answer_B.setGeometry(QtCore.QRect(130, 340, 61, 51))
        self.Answer_B.setObjectName("Answer_B")
        self.Answer_C = QtWidgets.QPushButton(self.page_2)
        self.Answer_C.setGeometry(QtCore.QRect(230, 340, 61, 51))
        self.Answer_C.setObjectName("Answer_C")
        self.Answer_D = QtWidgets.QPushButton(self.page_2)
        self.Answer_D.setGeometry(QtCore.QRect(330, 340, 61, 51))
        self.Answer_D.setObjectName("Answer_D")
        self.stackedWidget_initial.addWidget(self.page_2)
        self.stackedWidget_initial.raise_()
        self.groupBox.raise_()

        # Troca de questão

        self.Answer_A.clicked.connect(lambda: vq.verifyA(vq.placar))
        self.Answer_B.clicked.connect(lambda: vq.verifyB(vq.placar))
        self.Answer_C.clicked.connect(lambda: vq.verifyC(vq.placar))
        self.Answer_D.clicked.connect(lambda: vq.verifyD(vq.placar))
        self.pushButton.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_2.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_2.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_3.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_3.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_4.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_4.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_5.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_5.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_6.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_6.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_7.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_7.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_8.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_8.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_9.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_9.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_10.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_10.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_11.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_11.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_12.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_12.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_13.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_13.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_14.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_14.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_15.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_15.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))
        self.pushButton_16.clicked.connect(
            lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))
        self.pushButton_16.clicked.connect(
            lambda: self.label_2.setPixmap(QtGui.QPixmap(vq.rngen())))

        self.retranslateUi(MathMines)
        QtCore.QMetaObject.connectSlotsByName(MathMines)

    def retranslateUi(self, MathMines):
        _translate = QtCore.QCoreApplication.translate
        MathMines.setWindowTitle(_translate("MathMines", "Dialog"))
        self.label.setText(_translate("MathMines", "MathMines"))
        self.Answer_A.setText(_translate("MathMines", "A"))
        self.Answer_B.setText(_translate("MathMines", "B"))
        self.Answer_D.setText(_translate("MathMines", "D"))
        self.Answer_C.setText(_translate("MathMines", "C"))
        #self.label_2.setText(_translate("MathMines", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MathMines = QtWidgets.QDialog()
    ui = Ui_MathMines()
    ui.setupUi(MathMines)
    MathMines.show()
    sys.exit(app.exec_())