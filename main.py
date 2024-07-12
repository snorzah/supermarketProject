from supermarketFunctions import customerMode, adminMode
if __name__ == '__main__':
  items = {1 : ["Strawberry", 1.99],
           2 : ["Banana", 0.99],
           3 : ["Apple", 3.99],
           4 : ["Orange", 2.99],
           5 : ["Grapes", 4.99],
           6 : ["Cherry", 5.99]}
  finalPrice = 0
  intInputVar = 0
  while True:
    adminInput = input("Administrator or Customer settings? ('admin' for administrator or 'customer' for customer) ").upper()
    if (adminInput == 'CUSTOMER'):
        customerMode(items)
    elif (adminInput == 'ADMIN'):
        adminPassword = input("Please Enter Admin Password: ")
        if (adminPassword == '1234'):
            adminMode(items)
        customerMode(items)
        break
    else:
        print("Please Enter a Valid Input")
        print(" ")
