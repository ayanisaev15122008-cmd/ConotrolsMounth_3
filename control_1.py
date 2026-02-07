import os
from datetime import datetime

def load_history():
    if os.path.exists("history.txt"):
        with open("history.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()][-5:]
    return []

def save_history(data):
    with open("history.txt", "w", encoding="utf-8") as f:
        for item in data:
            f.write(item + "\n")

history = load_history()

while True:
    print("\n-ИСТОРИЯ (последние 5) -")
    for entry in history: print(entry)
    if not history: print("[пусто]")

    name = input("\nИмя (0 - очистить, выход - закрыть): ").strip()

    if name == "0":
        if os.path.exists("history.txt"): os.remove("history.txt")
        history = []
        print(">>> Очищено!")
        continue  

    if name.lower() == "выход":
        break

    if name:
        entry = f"[{datetime.now().strftime('%H:%M')}] Привет, {name}!"
        history.append(entry)
        history = history[-5:]
        save_history(history)
