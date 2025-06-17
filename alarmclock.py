import datetime
import time
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound="audio.mp3"
    running=True
    while running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time==alarm_time:
            print("Thoongunathu Pooothum daaa naaayeeeee!!🔊🔊")
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
                
            running=False
        time.sleep(1)
        


if __name__=="__main__":
    alarm_time=input("enter the alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)