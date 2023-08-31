import random
x = 1

for i in range(16):
    x = x + 1
    print(f"self.pushButton_%d.clicked.connect(lambda: self.stackedWidget_initial.setCurrentWidget(self.page_2))" % x)
    print(f"self.pushButton_%d.clicked.connect(lambda: self.label_2.setPixmap(QtGui.QPixmap(rngen())))" % x)