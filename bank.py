import json



def load_account():
    try:
        with open("bank_details.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_account(account):
    with open("bank_details.txt",'w') as file:
        json.dump(account,file)

def details(data):
    print("*" * 130)
    print("\n")
    if not data:
        print("No account details available.")
    else:
        for account, info in data.items():
            print(f"Account: {account} | Name: {info['name']} | Balance: {info['amount']}")
    print("\n")
    print("*" * 130)


def deposit(data,account,name,amount):
    data[account]={'name':name,'amount':amount}
    data[account]['amount']+=amount
    print(f"\n {amount} is Deposited to your account XXXX{account} \n")

def withdraw(data,account,amount):
    data[account]['amount']-=amount
    print(f"\n {amount} is withdrawal from your account {account}. \n")

def delete(data):
    prev=data['']
    data['account']="invalid"
    data['balance']=0
    print("*"*130)
    print("\n")
    print(f"Your account with {prev} is blocked !")
    print(f"Account:{data['account']} | Balance:{data['balance']}")
    print("\n")
    print("*"*130)

    

def main():
    data={}

    while True:
        print("STATE BANK OF INDIA | Our service is for you !")
        print("1. Check the current balance of the account !")
        print("2. Depositing the amount to the account !")
        print("3. Withdraw the amount from the account !")
        print("4. Blocking the bank account !")
        print("5. Exit from the Bank !")

        choice=input("Enter any option according to your conveience :")

        if choice=='1':
            details(data)
        
        elif choice=='2':
            details(data)
            account=input("enter your account number :")
            name=input("enter your name :")
            amount=int(input("enter the money to be deposited :"))
            deposit(data,account,name,amount)

        elif choice=='3':
            details(data)
            account=input("enter your account number :")
            amount=int(input("enter the money to be withdraw :"))
            withdraw(data,account,amount)

        elif choice=='4':
            delete(data)

        elif choice=='5':
            break
        else:
            print("please enter the valid option !")

if __name__=="__main__":
    main()
        
        

# data={'account1':["vaibhav",500] , 'account2':["drishti",1000]}

    # print(data['account1'][0]) ---> vaibhav
    # print(data['account1'][1]) ---> 500