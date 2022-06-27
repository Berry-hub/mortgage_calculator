from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon, QFont, QPixmap
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mortgage calculator')
        self.setWindowIcon(QIcon('money_icon.png'))
        self.setStyleSheet('background-color: tan')
        self.setGeometry(500,200, 800,600)

        self.background = QLabel(self)
        pixmap = QPixmap('background.png')
        pixmap = pixmap.scaled(508, 351)
        self.background.setPixmap(pixmap)

        self.setupGUI()


    def setupGUI(self):
        self.label = QLabel('', self)
        # self.label.setGeometry(500,50, 100,60)
        # self.label.setStyleSheet('background-color: transparent')
        # self.label.setFont(QFont('Arial', 12))
        self.loan_amount = QLineEdit('Total loan amount', self)
        self.interest_rate = QLineEdit('Annual interest rate', self)
        self.duration_years = QLineEdit('Duration in years', self)
        self.btn = QPushButton('Calculate monthly payment', self)
        # btn.setGeometry(100,100, 80,40)
        # btn.setStyleSheet('background-color: pink')
        # btn.setFont(QFont('Arial', 12))

        self.box = QGridLayout()
        self.box.addWidget(self.loan_amount, 0, 0)
        self.box.addWidget(self.interest_rate, 1, 0)
        self.box.addWidget(self.duration_years, 2, 0)
        self.box.addWidget(self.btn, 1, 1)
        self.box.addWidget(self.label, 2, 1)
        self.box.addWidget(self.background, 3, 1)
        self.setLayout(self.box)


        self.btn.clicked.connect(self.calculate)


    def calculate(self):
        loan = float(self.loan_amount.text())
        interest = float(self.interest_rate.text()) / 100 / 12
        duration = float(self.duration_years.text()) * 12
        formula = loan * (interest * (1.0 + interest) ** duration) / ((1.0 + interest) ** duration - 1.0)
        result = "{:.2f} CZK".format(formula)

        self.label.setText(result)
        self.label.setFont(QFont('Arial', 18))

        # print(formula)



        # self.label.setText(self.result.text())

        # self.label.setStyleSheet('background-color:red')



# M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]

# P = principal loan amount

# i = monthly interest rate

# n = number of months required to repay the loan



 




app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())



# M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]

# P = principal loan amount

# i = monthly interest rate

# n = number of months required to repay the loan