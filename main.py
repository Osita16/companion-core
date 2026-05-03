import datetime
import time
import json
from reminder import set_reminder
from motivation import get_motivation

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(data):
    with open("memory.json", "w") as f:
        json.dump(data, f)

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        print("Oshii: Good morning 🌿")
    elif hour < 18:
        print("Oshii: Good afternoon ☀️")
    else:
        print("Oshii: Good evening 🌙")

def tell_time():
    now = datetime.datetime.now().strftime("%H:%M")
    print(f"Oshii: It's {now}")

def main():
    memory = load_memory()
    greet()

    while True:
        user = input("\nYou: ").lower()

        if "time" in user:
            tell_time()

        elif "remind" in user:
            set_reminder()

        elif "motivate" in user:
            print("Oshii:", get_motivation())

        elif "goal" in user:
            goal = input("Tell me your goal: ")
            memory["goal"] = goal
            save_memory(memory)
            print("Oshii: Got it. I’ll remember this 💚")

        elif "exit" in user:
            print("Oshii: Take care 🌿")
            break

        else:
            print("Oshii: I’m still learning… tell me more.")

if __name__ == "__main__":
    main()