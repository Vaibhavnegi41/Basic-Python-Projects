def main():
    print("******WELCOME TO THE PYTHON QUIZ********")
    print("There will be 5 questions , each of 1 marks !")
 
    score=0

    result=input("who is the father of python ? - ")
    if result.lower()=="guido van rossuw":
        print("correct answer dear !")
        score+=1
    else:
        print("incorrect answer !")

    result=input("in which year python build ? -")
    if result=="1989":
        print("correct answer dear !")
        score+=1
    else:
        print("incorrect answer !")

    result=input("Tell me Pyhton is complied or interpreted language ? -")
    if result.lower()=="interpreted":
        print("correct answer dear !")
        score+=1
    else:
        print("incorrect answer !")

    result=input("What is the latest version of Python ? -")
    if result=="3.13.5":
        print("correct answer dear !")
        score+=1
    else:
        print("incorrect answer !")

    result=input("What is full form of OOPS ? -")
    if result=="object oriented programming":
        print("correct answer dear !")
        score+=1
    else:
        print("incorrect answer !")

    
    print("You got"+str(score)+" correct answer !")
    print("you got "+str((score / 5)*100)+" %.")

if __name__=="__main__":
    main()

    