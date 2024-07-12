def customerMode(items):
  print("Welcome, Valued Customer!")
  finalPrice = 0
  while True:
    inputVar = input('Please Scan the Barcode (To finish, type "pay"): ')
    if (inputVar.upper() == "SHUT DOWN"):
        adminPassCheck = input("Please Enter Admin Password: ")
        if adminPassCheck == '1234':
            break

    try:
        intInputVar = int(inputVar)
    except Exception:
      if (inputVar.upper() == 'PAY'):
        print("Your Total is:", round(finalPrice, 2))
        print(" ")
        finalPrice = 0
        print("Welcome, Valued Customer!")
        continue
      else:
        print("Please Enter a Valid Barcode.")
        continue

    if (intInputVar in items):
        finalPrice += items[intInputVar][1]
        print(f'you scanned "{items[intInputVar][0]}" for {items[intInputVar][1]}.')
        print(f"Your current total is {round(finalPrice, 2)}")
        print(" ")
    else:
        print("Please Enter a Valid Barcode.")
        print(" ")

def adminMode(items):
  print("Current Items: ")
  for i in items:
        print("barcode:", str(i) + ", name:", items[i][0] + ", price:", items[i][1])
  print(" ")
  while True:
    editOrNew = input("Add a New Item or Edit Existing Items? ('edit' or 'new') ").upper()
    if (editOrNew == "NEW"):
        adminAddName = input("What Item Name Would You Like to Add to the System? ").capitalize()
        adminAddPrice = input(f"What Price Should '{adminAddName}' Be? ")
        adminAddBarcode = input(f"What is the Barcode for '{adminAddName}?' ")
        try:
            adminAddPrice = float(adminAddPrice)
            adminAddBarcode = int(adminAddBarcode)
        except Exception:
            print("Please enter a valid price/barcode.")
            print(" ")
            continue
        if (adminAddBarcode not in items):
            items[adminAddBarcode] = [adminAddName, adminAddPrice]
            print(f"Successfully Added {adminAddName} to System With Barcode {adminAddBarcode} and Price {adminAddPrice}.")
            print(" ")
        else:
            print("Barcode Already in System.")
            print(" ")
    
    elif (editOrNew == "EDIT"):
        adminEditBarcode = input("What is the Barcode for the item you want to edit?' ")
        adminEditName = input("What Would You Like the New Name Be? ").capitalize()
        adminEditPrice = input(f"What Price Should '{adminEditName}' Be? ")
        try:
            adminEditPrice = float(adminEditPrice)
            adminEditBarcode = int(adminEditBarcode)
        except Exception:
            print("Please enter a valid price/barcode.")
            print(" ")
            continue
        if (adminEditBarcode in items):
            items[adminEditBarcode] = [adminEditName, adminEditPrice]
            print(f"Successfully Changed Name to {adminEditName} and Barcode to {adminEditBarcode} and Price to {adminEditPrice}.")
        else:
           print("Please Enter a Barcode in the System.")

    adminStop = input("Would you Like to Continue Adding/Editing Items? ('yes' or 'no') ")
    if (adminStop.upper() == 'NO'):
        print("Stopping...")
        print(" ")
        break
  print(" ")
