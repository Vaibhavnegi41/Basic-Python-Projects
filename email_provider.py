import json

def load_data():
    try:
        with open("emails_provider.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError :
        return []
    
def save_data(emails):
    with open("emails_provider.txt",'w') as file:
        json.dump(emails,file)

def list_data(emails):
    print('\n')
    print("*"*120)

    for index,value in enumerate(emails,start=1) :
        print(f"{index}. Username :{value['name']} | Email-ID :{value['email']}")

    print('\n')
    print("*"*120)

def add_email(emails,name,email):
    emails.append({'name':name ,'email':email})
    save_data(emails)

def update_email(emails,index,name,email):
    if 1 <= index <= len(emails):
        emails[index-1]={'name':name , 'email':email}
        save_data(emails)

    else:
        print("invalid index-value of the user !")

def delete_email(emails,index):
    if 1 <= index <=len(emails):
        del emails[index-1]
        save_data(emails)
    else:
        print("invalid index-value of the user !")

def get_email(emails,name):
    flag=False
    for row in emails:
        if row['name'].lower()==name:
            print("\n")
            print("*"*130)
            print(f"{row['email']} is the Email Address of the user !")
            print("\n")
            print("*"*130)
            flag=True

    if flag==False:
        print("You entered the incorrect username !")
    

def main():
    emails=load_data()
    while True:
            print("Welcome to Email-provider | choose any option \n")
            print("1. List all the username and email !")
            print("2. Add  the new username and email !")
            print("3. Update the existing username and email !")
            print("4. Delete  the existing username and email !")
            print("5. Get email of the user !")
            print("6. Exit from the Provider ! \n")

            choice=input("enter your choice dear :")

            if choice=='1':
                list_data(emails)

            elif choice=='2':
                name=input("enter the username :")
                email=input("enter your email ID :")
                add_email(emails,name,email)

            elif choice=='3':
                list_data(emails)
                value=int(input("enter the index-value of the username :"))
                name=input("enter new username :")
                email=input("enter new email of username :")
                update_email(emails,value,name,email)

            elif choice=='4':
                list_data(emails)
                value=int(input("enter the index-value of the username :"))
                delete_email(emails,value)

            elif choice=='5':
                name=input("enter username for email ID :").lower()
                get_email(emails,name)

            elif choice=="6":
                break

            else:
                print("Invalid choice value !")
        


if __name__=="__main__":
    main()