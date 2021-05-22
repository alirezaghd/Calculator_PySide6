# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader



class windozmain(QMainWindow):
    def __init__(self):
        super(windozmain, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.btn_equal.clicked.connect(self.equal)
        self.ui.btn_sum.clicked.connect(self.sum)
        self.ui.btn_sub.clicked.connect(self.sub)
        self.ui.btn_mul.clicked.connect(self.mul)
        self.ui.btn_div.clicked.connect(self.div)
        self.ui.btn_per.clicked.connect(self.per)
        self.ui.btn_f.clicked.connect(self.dot)
        self.ui.btn_ch.clicked.connect(self.change)
        self.ui.btn_ac.clicked.connect(self.ac)
        self.ui.btn_1.clicked.connect(self.num1)
        self.ui.btn_2.clicked.connect(self.num2)
        self.ui.btn_3.clicked.connect(self.num3)
        self.ui.btn_4.clicked.connect(self.num4)
        self.ui.btn_5.clicked.connect(self.num5)
        self.ui.btn_6.clicked.connect(self.num6)
        self.ui.btn_7.clicked.connect(self.num7)
        self.ui.btn_8.clicked.connect(self.num8)
        self.ui.btn_9.clicked.connect(self.num9)
        self.ui.btn_0.clicked.connect(self.num0)

    def num1(self):
        #self.ui.tb1.setText(self.ui.tb1.text() + '1' )
        t = self.ui.tb1.text()
        t = t + '1'
        self.ui.tb1.setText(t)

    def num2(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '2')

    def num3(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '3')

    def num4(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '4')

    def num5(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '5')

    def num6(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '6')

    def num7(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '7')

    def num8(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '8')

    def num9(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '9')

    def num0(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '0')

    def dot(self):
        self.ui.tb1.setText(self.ui.tb1.text() + '.')

    def equal(self):

        self.b = float(self.ui.tb1.text())

        if self.op == '+':
            result = self.a + self.b
        elif self.op == '-':
            result = self.a - self.b

        elif self.op == '*':
            result = self.a * self.b

        elif self.op == '/':
            if self.b == 0:
                self.ui.tb2.setText("تقسیم بر صفر نداریم")
            else:
                result = self.a / self.b
        elif self.op == '%':
            result = self.a * 0.01

        self.ui.tb1.setText(str(result))
        self.ui.tb2.setText(str(self.a) + ' ' + str(self.op) + ' ' + str(self.b))

    def sum(self):
        self.op = '+'
        self.a = float(self.ui.tb1.text())
        self.ui.tb1.clear()

    def sub(self):
        self.op = '-'
        self.a = float(self.ui.tb1.text())
        self.ui.tb1.clear()

    def mul(self):
        self.op = '*'
        self.a = float(self.ui.tb1.text())
        self.ui.tb1.clear()

    def div(self):
        self.op = '/'
        self.a = float(self.ui.tb1.text())
        self.ui.tb1.clear()

    def per(self):
        self.op = '%'
        self.a = float(self.ui.tb1.text())

    def change(self):

        self.a = float(self.ui.tb1.text())
        self.a *= -1
    def ac(self):
        #self.a = float(self.ui.tb1.text())
        self.ui.tb1.clear()
        self.a = self.ui.tb1.setText(self.ui.tb1.text() + '0')






if __name__ == "__main__":
    app = QApplication([])
    window = windozmain()
    sys.exit(app.exec_())
