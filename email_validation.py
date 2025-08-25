string="negivaibhav2005@gmail.com"
idx=string.index("@")

if string[idx+1:] == "gmail.com" :
    print("yes")

def email_generate():
    email=input("enter your email please :")
    return email

def main():
    while True:
        print("Email Validation Step | choose any option ! \n")
        print("1. Pick Email for International use !")
        print("\t1.1 Choose for commercial use (.com) !")
        print("\t1.2 Choose for organizational use (.org) !")
        
        print("\n2. Pick Email for country-code domain !")
        print("\t2.1 Choose for India Government !")
        print("\t2.2 Choose for United Kingdom Government !")

        choice=input("Choose any one option for Email format :")

        if choice=='1.1':
            email=email_generate()
            if email[0].isalpha() and len(email) < 6:
                if '@' in email:
                    idx=email.index('@')
                else:
                    print("INvlid email does not contain @ in the format !")
                if email[idx+1:]=="gmail.com" and " " not in email and email.count('@')==1 and email.count(".")==1 :
                    print("\n**********Valid Email added successsfully !************\n")
                else:
                    print("Invalid email , does not satisfy guidelines !")
        
            else:
                print("Invalid email Starting with numeric value !")

        elif choice=='1.2':
            email=email_generate()
            if email[0].isalpha() and len(email) < 6:
                idx=email.index('.')
                if email[idx+1:]=="org" and " " not in email and email.count('@')==1 and email.count(".")==1 :
                    print("\n*********Valid Email added successsfully !***********\n")
                else:
                    print("Invalid email , does not satisfy guidelines !")
        
            else:
                print("Invalid email Starting with numeric value !")


        elif choice=='2.1':
            email=email_generate()
            if email[0].isalpha() and len(email) < 6:
                idx=email.index('@')
                if  ( email[idx+1:]=="@gov.in" or email[idx+1:]=="@nic.in" ) and " " not in email and email.count('@')==1 and email.count(".") :
                    print("\n**********Valid Email added successsfully !**********\n")
                else:
                    print("Invalid email , does not satisfy guidelines !")
        
            else:
                print("Invalid email Starting with numeric value !")

        elif choice=='2.2':
            email=email_generate()
            if email[0].isalpha() and len(email) < 6:
                idx=email.index('.')
                if email[idx+1:]=="gov.uk" and " " not in email and email.count('@')==1 and email.count(".") :
                    print("\n**********Valid Email added successsfully !**************\n")
                else:
                    print("Invalid email , does not satisfy guidelines !")
        
            else:
                print("Invalid email Starting with numeric value !")

        else:
            print("invalid option choosed by you dear !")

if __name__=="__main__":
    main()

            

