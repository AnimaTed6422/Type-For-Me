import keyboard
import os
import time

def type(message):
    for char in message:
        keyboard.press_and_release(message)
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
        if(char.isupper()):
            keyboard.press_and_release("shift + " + char)
        elif(char == "!" or "@" or "#" or "$" or "%" or "^" or "&" or "*" or "(" or ")" or "{" or "}" or "?" or "<" or ">" or "~" or ":" or "\""):
            type("shift + " + char)
        else:
            keyboard.press_and_release(char)
        time.sleep(0.00001)
    pause()
