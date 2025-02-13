import time
import pyautogui
import tkinter as tk
import random
import string
from tkinter import simpledialog

global use_moderate_speed
use_moderate_speed = False

def toggle_speed():
    global use_moderate_speed
    use_moderate_speed = not use_moderate_speed
    speed_button.config(bg="green" if use_moderate_speed else "red", text="Slow" if use_moderate_speed else "Fast")

def simulate_typing(text, typing_speed):
    """
    Simulates typing the given text at the specified typing speed (characters per second).
    
    :param text: The text to type
    :param typing_speed: The typing speed in characters per second
    """
    time.sleep(2.5)  # You can customise this so theres less delay when you click type
    
    total_chars = len(text)
    if total_chars == 0:
        return
    
    delay_per_char = 1 / typing_speed
    
    for char in text:
        pyautogui.write(char)
        time.sleep(delay_per_char)

def type_instantly():
    """Waits before typing the text instantly."""
    time.sleep(2.5)
    text_to_type = text_entry.get()
    pyautogui.write(text_to_type)

def spam_random_chars():
    """Waits before spamming a random string of the selected length instantly or at moderate speed."""
    time.sleep(2.5)
    try:
        char_count = int(spam_entry.get())
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=char_count))
        if use_moderate_speed:
            for char in random_text:
                pyautogui.write(char)
                time.sleep(0.05)
        else:
            pyautogui.write(random_text)
    except ValueError:
        result_label.config(text="Please enter a valid number for character count.")

def start_typing():
    text_to_type = text_entry.get()
    try:
        typing_speed = float(speed_entry.get())
        simulate_typing(text_to_type, typing_speed)
    except ValueError:
        result_label.config(text="Please enter a valid number for typing speed.")

# Create GUI
root = tk.Tk()
root.title("Auto Typing")
root.attributes('-topmost', 1)

tk.Label(root, text="Enter text:").pack()
text_entry = tk.Entry(root, width=50)
text_entry.pack()

tk.Label(root, text="Typing speed (characters per second):").pack()
speed_entry = tk.Entry(root, width=10)
speed_entry.pack()

tk.Button(root, text="Start Typing", command=start_typing).pack()
tk.Button(root, text="Type Instantly", command=type_instantly).pack()

tk.Label(root, text="Spam random characters (length):").pack()
spam_entry = tk.Entry(root, width=10)
spam_entry.pack()

tk.Button(root, text="Spam Random Characters", command=spam_random_chars).pack()
speed_button = tk.Button(root, text="Fast", bg="red", width=10, height=2, command=toggle_speed)
speed_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()