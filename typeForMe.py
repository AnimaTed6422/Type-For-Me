import keyboard
import os
import time

os.system("title Type For Me!")
def pause():
    input("Press Enter To Continue...")
while(True):
    sen = input("Copy & Paste Text Below\n")
    print("You have 5 Seconds")
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    for char in sen:
        if(char == "!"):
            keyboard.press_and_release("shift + 1")
        else:
            if(char.isupper()):
                keyboard.press_and_release("shift + " + char)
            else:
                keyboard.press_and_release(char)
            time.sleep(0.00000000000000000000000001)
    pause()
