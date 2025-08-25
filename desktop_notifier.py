from plyer import notification
import time

if __name__=="__main__":


    while True:


        notification.notify(
            title="******Take Rest *******",
            message="Rest is vital for good mental health , reduces stress and anxiety !",
            timeout=5
        )


        time.sleep(20)