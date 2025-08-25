import random
import sqlite3 as sq

special=['!','@','#',"$",'%',"&"]
alpha=['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m']
capital=['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
digit=['1','2','3','4','5','6','7','8','9','0']

connection=sq.connect("passwords.db")

cursor=connection.cursor()

cursor.execute('''

     CREATE TABLE IF NOT EXISTS passwords(
               id INT PRIMARY KEY,
               name TEXT NOT NULL,
               password TEXT NOT NULL
               )    
''')

def add_password(id,name,password):
    cursor.execute("INSERT INTO passwords (id,name,password) VALUES (?,?,?)",(id,name,password))
    connection.commit()
    print("\n Name and Password is added successfully !")

def list_all_passwords():
    cursor.execute("SELECT * FROM passwords ORDER BY id ASC")
    data=cursor.fetchall()
    print("\n")
    print("*"*130)
    for row in data:
        print(f"{row[0]}. {row[1]} | Password :{row[2]}")
    print("*"*130)
    print("\n")




def generator(min_length,has_number,has_special):
    count=0
    password=""

    while count <= min_length :
        
        choice=random.randint(1,4)

        if choice==1:
            idx=random.randint(0,25)
            password+=capital[idx]
            count+=1

        elif choice==2:
            idx=random.randint(0,25)
            password+=alpha[idx]
            count+=1

        elif choice==3 and has_number:
            idx=random.randint(0,9)
            password+=digit[idx]
            count+=1

        elif choice==4 and has_special:
            idx=random.randint(0,5)
            password+=special[idx]
            count+=1


    return password


def main():

    while True:
        print("\n")
        print("*"*130)
        print("Password Generator and Storage | pick any option !")
        print("\n1. List all the passwords data !")
        print("2. Add new password with name !")
        print("3. Delete passwords from database !")
        print("4. Exit from the loop !")

        choice=int(input("enter your choice dear :"))

        if choice==1:
            list_all_passwords()

        elif choice==2:
            id=int(input("enter the employee id :"))
            name=input("enter the employee name :")
            min_length=int(input("enter the minimum length of the password :"))
            has_number=input("Do you want to add the number ? (yes/no) :").lower() == "yes"
            has_special=input("Do you Want to add the special character ? (yes/no) :").lower() == "yes"
            password=generator(min_length,has_number,has_special)
            add_password(id,name,password)

        elif choice==3:
            pass

        elif choice==4:
            break

        else:
            print("Invalid option choice from your side dear !")


if __name__=="__main__":
    main()

connection.close()