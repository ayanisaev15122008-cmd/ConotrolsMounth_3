import tkinter as tk
HISTORY_FILE = "history.txt"

history = []

def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                history.append(line.strip())
                history_text.insert(tk.END, line)
    except FileNotFoundError:
        pass

def save_history():
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        for item in history:
            file.write(item + "\n")

def add_greeting():
    name = name_entry.get()
    if name == "":
        return

    greeting = f"Привет, {name}!"
    history.append(greeting)
    if len(history) > 5:
        history.pop(0)
    history_text.delete(1.0, tk.END)
    for item in history:
        history_text.insert(tk.END, item + "\n")
    save_history()

    name_entry.delete(0, tk.END)
window = tk.Tk()
window.title("Приветствия")
name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)
add_button = tk.Button(window, text="Поздороваться", command=add_greeting)
add_button.pack(pady=5)
history_text = tk.Text(window, width=40, height=10)
history_text.pack(pady=5)

load_history()

window.mainloop()