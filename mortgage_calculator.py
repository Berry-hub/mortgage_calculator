from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QListWidget
from PyQt6.QtGui import QIcon, QFont, QPixmap
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mortgage calculator')
        self.setWindowIcon(QIcon('money_icon.png'))
        self.setStyleSheet('background-color: tan')
        self.setGeometry(500,200, 800,500)

        self.background = QLabel(self)
        pixmap = QPixmap('background.png')
        pixmap = pixmap.scaled(508//2, 351//2)
        self.background.setPixmap(pixmap)

        self.setupGUI()

    def setupGUI(self):
        self.loan_amount = QLineEdit('Total loan amount', self)
        self.interest_rate = QLineEdit('Annual interest rate', self)
        self.duration_years = QLineEdit('Duration in years', self)

        self.btn = QPushButton('Count monthly payment', self)
        self.btn.setStyleSheet('background-color: pink')
        self.btn.setFont(QFont('Arial', 12))
        self.result_payment = QLabel('', self)

        self.month_label = QLabel('month', self)
        self.interest_label = QLabel('interest', self)
        self.amortization_label = QLabel('amortization', self)
        # self.label.setStyleSheet('background-color: transparent')
        # self.label.setFont(QFont('Arial', 12))

        self.anum = QLabel('', self)
        self.interest_annual = QLabel('', self)
        self.amortization_annual = QLabel('', self)

        self.show_month = QListWidget()
        self.show_interest = QListWidget()
        self.show_amortization = QListWidget()

        self.box = QGridLayout()
        self.box.addWidget(self.loan_amount, 0, 0)
        self.box.addWidget(self.interest_rate, 1, 0)
        self.box.addWidget(self.duration_years, 2, 0)
        self.box.addWidget(self.btn, 1, 1)
        self.box.addWidget(self.result_payment, 2, 1)
        self.box.addWidget(self.month_label, 4, 0)
        self.box.addWidget(self.interest_label, 4, 1)
        self.box.addWidget(self.amortization_label, 4, 2)
        self.box.addWidget(self.background, 0, 2, 3, 1)
        self.box.addWidget(self.show_month, 5, 0)
        self.box.addWidget(self.show_interest, 5, 1)
        self.box.addWidget(self.show_amortization, 5, 2)
        self.box.addWidget(self.anum, 6, 0)
        self.box.addWidget(self.interest_annual, 6, 1)
        self.box.addWidget(self.amortization_annual, 6, 2)


        self.setLayout(self.box)

        self.btn.clicked.connect(self.calculate)


    def calculate(self):
        try: 
            loan = float(self.loan_amount.text())
            interest = float(self.interest_rate.text()) / 100 / 12
            duration = float(self.duration_years.text()) * 12
            monthly_payment = loan * (interest * (1.0 + interest) ** duration) / ((1.0 + interest) ** duration - 1.0)
            show_monthly_payment = "{:.2f} CZK".format(monthly_payment)
            self.result_payment.setText(show_monthly_payment)
            self.result_payment.setFont(QFont('Arial', 18))

            list_month = []
            list_interest = []
            list_amortization = []
            for i in range(12):
                list_month.append(str(int(i)+1))
                list_interest.append(loan * interest)
                loan = loan - (monthly_payment - list_interest[-1])
                list_amortization.append(monthly_payment - list_interest[-1])
            list_interest_str  = []
            list_amortization_str = []
            for value in list_interest:
                list_interest_str.append(str("{:.2f} CZK".format(value)))
            for value in list_amortization:
                list_amortization_str.append(str("{:.2f} CZK".format(value)))
            self.show_interest.addItems(list_interest_str)
            self.show_amortization.addItems(list_amortization_str)
            self.show_month.addItems(list_month)

            self.anum.setText('per anum')
            self.interest_annual.setText(str('{:.2f} CZK'.format(sum(list_interest))))
            self.amortization_annual.setText(str('{:.2f} CZK'.format(sum(list_amortization))))
            self.anum.setFont(QFont('Arial', 14))
            self.interest_annual.setFont(QFont('Arial', 14))
            self.amortization_annual.setFont(QFont('Arial', 14))

        except ValueError:
            print('you have to fill the numbers!')


app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())


