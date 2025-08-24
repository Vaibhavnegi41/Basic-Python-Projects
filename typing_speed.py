from time import *
import random

lines=["I am a good boy !","My name is Vaibhav Negi.","Visual Code is a type of open source IDE .",
       "IoT means interconnectedness of the objects using internet.",
       "Raspberry Pi is a modern microprocessor , used for controlling big automated projects ."]

def mistakes(given_para,typed_para):
    error=0

    for i in range(len(given_para)):
        try:
            if given_para[i] != typed_para[i]:
                error+=1
        
        except:
            error+=1

    return error

def calculation(start_time,end_time,typed_para):

    delays=end_time-start_time
    rounded_delays=round(delays,2)

    speed=len(typed_para)/rounded_delays

    return round(speed)

def main():

    while True:

        given_para=random.choice(lines)

        print("\nTyping Speed Calculator | Pick option either 1 or 2 ! \n")

        print("1.Would you like to check your typing skills ?")
        print("2.Would you like to EXIT ?")
        
        choice=int(input("\nEnter your choice dear :"))

        if choice==1:
            print("*"*130)
            print(given_para)
            print("*"*130)

            start_time=time()
            typed_para=input("\nEnter the paragraph :")
            end_time=time()

            errors=mistakes(given_para,typed_para)
            speed=calculation(start_time,end_time,typed_para)

            print("*"*130)
            print("Errors :",errors)
            print("Speed :",speed,"w/sec")
            print("*"*130)


        elif choice==2:
            break

        else:
            print("\n******You entered the invalid option !*****")


if __name__=="__main__":
    main()