from PyQt5.QtWidgets import QPushButton, QLabel, QPlainTextEdit,QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator,self).__init__()
        uic.loadUi("calculator.ui",self)
        self.setFixedSize(self.size())
        self.show()


        self.button_1.clicked.connect(lambda: self.add_one(self.inputbox_expression,self.label_result))
        self.button_2.clicked.connect(lambda: self.add_two(self.inputbox_expression,self.label_result))
        self.button_3.clicked.connect(lambda: self.add_three(self.inputbox_expression,self.label_result))
        self.button_4.clicked.connect(lambda: self.add_four(self.inputbox_expression,self.label_result))
        self.button_5.clicked.connect(lambda: self.add_five(self.inputbox_expression,self.label_result))
        self.button_6.clicked.connect(lambda: self.add_six(self.inputbox_expression,self.label_result))
        self.button_7.clicked.connect(lambda: self.add_seven(self.inputbox_expression,self.label_result))
        self.button_8.clicked.connect(lambda: self.add_eight(self.inputbox_expression,self.label_result))
        self.button_9.clicked.connect(lambda: self.add_nine(self.inputbox_expression,self.label_result))
        self.button_0.clicked.connect(lambda: self.add_zero(self.inputbox_expression,self.label_result))
        self.button_add.clicked.connect(lambda: self.add_add(self.inputbox_expression,self.label_result))
        self.button_subtract.clicked.connect(lambda: self.add_subtract(self.inputbox_expression,self.label_result))
        self.button_multiply.clicked.connect(lambda: self.add_multiply(self.inputbox_expression,self.label_result))
        self.button_divide.clicked.connect(lambda: self.add_divide(self.inputbox_expression,self.label_result))
        self.button_decimal.clicked.connect(lambda: self.add_decimal(self.inputbox_expression,self.label_result))
        self.button_percentage.clicked.connect(lambda: self.add_percentage(self.inputbox_expression,self.label_result))


        self.button_clearall.clicked.connect(lambda: self.clearall(self.inputbox_expression,self.label_result))
        self.button_clearone.clicked.connect(lambda: self.clearone(self.inputbox_expression,self.label_result))
        self.button_result.clicked.connect(lambda: self.result(self.inputbox_expression,self.label_result))


    def add_one(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"1")
        self.result(expression,result_bar)

    def add_two(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"2")
        self.result(expression, result_bar)
    def add_three(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"3")
        self.result(expression, result_bar)
    def add_four(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"4")
        self.result(expression, result_bar)
    def add_five(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"5")
        self.result(expression, result_bar)
    def add_six(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"6")
        self.result(expression, result_bar)
    def add_seven(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"7")
        self.result(expression, result_bar)
    def add_eight(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"8")
        self.result(expression, result_bar)
    def add_nine(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"9")
        self.result(expression, result_bar)
    def add_zero(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"0")
        self.result(expression, result_bar)
    def add_add(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"+")
        self.result(expression, result_bar)
    def add_subtract(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"-")
        self.result(expression, result_bar)
    def add_multiply(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"*")
        self.result(expression, result_bar)
    def add_divide(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"/")
        self.result(expression,result_bar)

    def add_decimal(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+".")
        self.result(expression,result_bar)

    def add_percentage(self,expression, result_bar):
        expression.setPlainText(expression.toPlainText()+"%")
        self.result(expression,result_bar)


    def clearall(self,expression, result_bar):
        expression.setPlainText("")
        self.result(expression, result_bar)

    def clearone(self,expression,result_bar):
        expression.setPlainText(expression.toPlainText()[0:len(expression.toPlainText())-1])
        self.result(expression,result_bar)

    def result(self, expression, result_bar):
        result = "error"
        expression = expression.toPlainText()
        try:
            if expression == "":
                result = ""
            elif expression[len(expression)-1] == '+' \
                or expression[len(expression)-1] == '-' \
                or expression[len(expression)-1] == '/' \
                or expression[len(expression)-1] == '*' :
                res = eval(expression[0:len(expression)-1])
                result = res

            else:
                res = eval(expression)
                result= res
        except Exception :
            result = "error in expression"

        result_bar.setText(str(result) + "=")


if __name__ == '__main__':
    app = QApplication([])
    window = Calculator()
    app.exec_()

