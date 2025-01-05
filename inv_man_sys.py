def management_sys():
    items = []  

    def add_item():
        name = input("Enter name of the item: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        item = {"name": name, "quantity": quantity, "price": price}
        for item in items:
          if item["name"].lower()==name.lower():
            print("item already exists")
            break
        else:
            items.append(item) 
            print("item added sucessfully")
        
        
    def update_item():
        name = input("Enter the name of the item to update: ")
        for item in items:
            if item["name"].lower() == name.lower():
                new_quantity = int(input("Enter the new quantity: "))
                item["quantity"] = new_quantity
                print("quantity updated")
                break
    
        else:
            print("Item not found!")
    def delete_item():
      name = input("Enter the name of the item to delete: ")
      for item in items:
            if item["name"].lower() == name.lower():
              items.remove(item)
              print("item deleted")
              break
      else:
        print("item not found")

    while True: 
        op = input("Enter the operation to be performed (ADD, UPDATE, DELETE, TOTAL, EXIT): ").upper()
        if op == "ADD":
            add_item()
        elif op=="UPDATE":
            update_item()
        elif op=="DELETE":
            delete_item()
        elif op == "TOTAL":
            total = sum(item['quantity'] * item['price'] for item in items)
            print(f"Total value of items: {total}")
        elif op == "EXIT":
            print("Exiting the system.")
            break
        else:
            print("Invalid operation. Please try again.")
    print(items)

management_sys()


  
