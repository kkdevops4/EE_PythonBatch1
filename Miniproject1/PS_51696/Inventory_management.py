#WAP for Inventory management  
# 1.Functionalites involved  add products 
# 2.Sell and restock products
# 3.Alert when low stock
# 4. Report
global medico_data
medico_data=[]

def medicine_info():
    name=input("enter name of medicine :")
    batch=input("enter the batch name :")
    expiry=input("enter the xpiry date :")
    price= float(input("enter the price :"))
    quantity=int(input("enter the quantity :"))
    reorder_level=int(input("enter the reorder threshold :"))
    
    medicine= {"name": name , "batch": batch, "expiry": expiry ,"price":price , "quantity": quantity, "reorder_level": reorder_level}
    medico_data.append(medicine)
    print("data has been sucessfully stored")

def sell_medicine():
    name=input('name of medicine')
    found=False

    for i in medico_data:
        if i["name"].lower()== name.lower():
            found=True
            qty_to_sell=int(input(f"enter the quantity to see (available :{i["quantity"]}): "))
            
            if qty_to_sell>i["quantity"]:
                print('not enough')
                return
            
            i["quantity"]-=qty_to_sell
            total=i["price"]*qty_to_sell
            print(f"sold {qty_to_sell} units .Total bill {total}")
        if not found:
           print('the medicine not found')

def restock():
    name=input("enter name of thr medicine")
    found=False
    for i in medico_data:
        if i["name"].lower()== name.lower():
            found=True
            qty=int(input("enter the quantity : "))
            i["quantity"]+=qty
            print(f"the restocked item {name} in {qty} units. new quantity {i['quantity']}")
    if not found:
        print("medicine not found")

          
# low stock indicator 

def show_low_stock():
    print("\n--- Low Stock Medicines ---")
    low_found= False

    for i in medico_data:
        if i["quantity"] <= i["reorder_level"]:
            low_found=True
            print(f"name :{i['name']}")
            print(f"Batch: {i["batch"]}")
            print(f"quantity : {i["quantity"]} (reorder level : {i["reorder_level"]})")
            print("-"*30)

    if not low_found:
        print("no medicines below reorder level")

def main_menu():
    while True:
        print("\n simple Inventory Manager")
        print ("1.Add product")
        print("2. Sell product")
        print("3. Restock product")
        print("4. Show low-stock products ")
        print("5. Show all products")
        print("6. Exit ")

        Choice=input("Enter your choice (1-6) :")
        if Choice== "1":
            medicine_info()
        elif Choice== "2":
            sell_medicine()
        elif Choice=="3":
            restock()
        elif Choice=="4":
            show_low_stock()
        elif Choice=="5":
            print("\n---all products--- ")
            for p in medico_data:
                print(f"name: {p["name"]}, price : rs {p["price"]:.2f}, Quantity:{p["quantity"]}")
        elif Choice== "6":
            print("goodbye!")
            break
        else:
            print("Invalid choice. Try again")

main_menu()