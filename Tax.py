__author__ = 'jc350024'





def tax_return(income):
    if income <= 16000:
        return 0
    else:
        return(income-16000)*0.3

income =float(input("Income:"))
tax = tax_return(income)
if tax == 0:
    print("no tax")
else:
    print(tax)