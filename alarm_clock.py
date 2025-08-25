from playsound import playsound
import time

CLEAR="\033[2J" #IT CAN CLEAR THE TERMINAL AND THEN EXECUTE WHAT YOU WANT 
CLEAR_AND_RETURN="\033[H" #if we want to execute something after and after like a clock ticking then we use it


def alarm(seconds):

    time_elapsed=0
    print(CLEAR)

    while time_elapsed < seconds:
        
        time.sleep(1)
        time_elapsed+=1

        time_left=seconds-time_elapsed
        minute_left=time_left // 60
        seconds_left=time_left % 60

        print(f"{CLEAR_AND_RETURN} Alarm will sound in :{minute_left:02d}:{seconds_left:02d}") 
        #making single digit minutes and seconds into double digits
    
    playsound(r"C:\Users\VAIBHAV NEGI\OneDrive\Desktop\python\basic_projects\alarm.mp3")

minutes=int(input("How many minutes you want to wait :"))
seconds=int(input("How many seconds you want to wait :"))

total_seconds=minutes*60+seconds
alarm(total_seconds)