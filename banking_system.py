import json
import random

balance=500

def load_bank_data():
    try:
        with open("bank_details.txt",'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
def save_details(bank_data):
    with open("bank_details.txt",'w') as file:
        json.dump(bank_data,file)


def account_details(bank_data):
    print('\n')
    print("*"*130)
    idx=1
    for row in bank_data:
        print(f"{idx}. Account No. :{row['account']} | Holder Name :{row['name']} | Balance :{row['balance']}")
        idx+=1
    # for index,value in enumerate(bank_data,start=1):
    #     print(f"{index}. Account No. :{value['account']} | Holder Name :{value['name']} | Balance: {value['balance']}")

    print('\n')
    print("*"*130)

def deposit(bank_data,account,amount):

    for row in bank_data:
        if row['account']==account:
            row['balance']+=amount
            print('\n')
            print("*"*130)
            print(f"{amount} is deposited to your account XXX{account} | Current Amount :{row['balance']}!")
            print('\n')
            print("*"*130)
    
    save_details(bank_data)
    

def withdraw(bank_data,account,amount):

    for row in bank_data:
        if row['account']==account:
            row['balance']-=amount
            print('\n')
            print("*"*130)
            print(f"{amount} is withdrawal to your account XXX{account} | Current Amount:{row['balance']} !")
            print('\n')
            print("*"*130)
    
    save_details(bank_data)

def delete(bank_data,account):
    
    # for i,row in enumerate(bank_data):
    #     if row['account']==account:
    print(f"\n {account} is blocked ! \n Thank you for your support and trust dear ! \n")
            # del bank_data[i]
            # break

    bank_data=[row for row in bank_data if row['account']!=account]
    save_details(bank_data)


def open_account(bank_data,account,name,balance):
    bank_data.append({'account':account,'name':name,'balance':balance})
    save_details(bank_data)

# [{'account':dasdasd,"name":dadasd,'balance':2323},{},{},{}]

def main():

    bank_data=load_bank_data()

    while True:

        print("Bank Of Baroda | pick any option --")
        print("1.Provide account holder details !")
        print("2.Deposit money in the account !")
        print("3.Withdraw money from the account !")
        print("4.Delete account from the bank !")
        print("5. Opening new account in bank !")
        print("6. Exit from the bank ! \n")

        choice=input("enter your choice please :")

        if choice=='1':
            account_details(bank_data)
        
        elif choice=='2':
            account_details(bank_data)
            account=input("enter account number :")
            amount=int(input("enter amount to be deposited :"))
            deposit(bank_data,account,amount)

        elif choice=='3':
            account_details(bank_data)
            account=input("enter your acciunt number :")
            amount=int(input("enter the amount to be withdrawal from account :"))
            withdraw(bank_data,account,amount)

        elif choice=='4':
            account_details(bank_data)
            account=input("enter account number to be deleted :")
            delete(bank_data,account)
        
        elif choice=='5':
            digits=['3','1','5','6','2','9','7','4','8']
            account=""
            for i in range(len(digits)):
                idx=random.randint(0,len(digits)-1)
                account=account+digits[idx]
            
            print(account)
            name=input("enter account holder name :")
            open_account(bank_data,account,name,balance)
        
        elif choice=='6':
            break

        else:
            print("You choose invalid choice !")


if __name__=="__main__":
    main()