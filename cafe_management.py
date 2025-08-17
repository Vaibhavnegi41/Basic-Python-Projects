cafe={'1':["Margherita Pizza",50],'2':["Cheese Garlic Bread",100],'3':["red sauce pasta",120],
      '4':["Chilly Potato",50],'5':["Cold coffee",60]}


# this fundtion is basically for counting the food items and it returns the dictionary with 
# key-value of food name with its total counts..............................................
def count_items(orders):
    old=[]
    name=[]
    d={}
    for value in orders:
        name.append(value[0])
    print(name)

    for item in name:
        if item not in old:
            total=name.count(item)
            old.append(item)
            d[item]=total
    
    return d
    
    

    
# this function receiving count of food item from the upper function and build a bill 
# receipt with quantity adn amount of food item......................................
def ordered_records(orders,amount):
    data=[]
    count_dict=count_items(orders)
    
    print("*"*120)
    print("$$$$ Food Order Bill $$$$\n")
    if(len(orders)==0):
        print("hey buddy, you did not ordered yet ! | Thank you dear !")
    idx=1
    for dish in orders:
        if dish[0] not in data:
            print(f"{idx}. {dish[0]} | Quantity: {count_dict[dish[0]]} | Amount: {count_dict[dish[0]] * dish[1]}Rs")
            data.append(dish[0])
            idx+=1
    print("\n Total Bill :",amount,"Rs")
    print("\n")
    print("*"*120)



# it is a main function used for taking orders from the customers
def main():
    orders=[]
    amount=0
    while True:
        print("Welcome to Cafe With Bro | Tell me your order ! \n")
        print("1.Margherita Pizza-50rs \n 2.Cheese Garlic Bread-100rs \n 3.Red Sauce Pasta-120rs \n 4.Chilly Potato-50rs \n 5.Cold Coffee-60rs \n 6.Want Bill?")
        print('\n')
        choice=input("enter serial number for your next order :")
        if(choice=='6'):
            break

        amount+=cafe[choice][1]
        orders.append([cafe[choice][0],cafe[choice][1]])
        print("Your food has been successfully ordered ! \n")
    
    ordered_records(orders,amount)
    



if __name__=="__main__":
    main()