import time

def set_reminder():
    msg = input("What should I remind you about? ")
    sec = int(input("After how many seconds? "))

    print("Oshii: Reminder set ⏳")

    time.sleep(sec)

    print(f"\nOshii Reminder: {msg}")