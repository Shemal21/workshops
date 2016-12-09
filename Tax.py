__author__ = 'jc350024'

tax_return =0
income = float(input("Income:"))
if income > 16000:
    tax = (income - 16000)*0.3
    print(tax)

def tax_return(income):
    if income <= 16000:
        return 0
    else:
        return(income-16000)*0.3
