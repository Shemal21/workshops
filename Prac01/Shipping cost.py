__author__ = 'jc350024'

Instruction = "Welcome to our program.\nInput negative number into number of Item to quit"
print (Instruction)

numOfItems = 1
while numOfItems > 0 :

    numOfItems = int(input("Please input the number of Item: "))
    costPerItem = float(input("The shipping Cost for each Item:$ "))

    totalShippingCost = numOfItems * costPerItem;

    if totalShippingCost > 100:
       totalShippingCost = totalShippingCost * 0.9

    print("The total cost for delivering your product is: ",totalShippingCost)



