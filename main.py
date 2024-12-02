import customtkinter as ctk
import pyautogui
import threading
import time

# Global variables
clicking = False  # To control the clicking loop
interval = 0.1  # Default interval between clicks (in seconds)

# Function to perform the clicking
def start_clicking():
    global clicking
    while clicking:
        pyautogui.click()
        time.sleep(interval)

# Start button callback
def start_clicking_thread():
    global clicking
    if not clicking:
        clicking = True
        thread = threading.Thread(target=start_clicking)
        thread.start()

# Stop button callback
def stop_clicking():
    global clicking
    clicking = False

# Function to update the interval based on user input
def update_interval(value):
    global interval
    interval = float(value)

# Setting up the GUI
app = ctk.CTk()  # Initialize the customtkinter window
app.geometry("300x200")
app.title("Python Autoclicker")

# Title Label
title_label = ctk.CTkLabel(app, text="Autoclicker", font=("Arial", 18))
title_label.pack(pady=10)

# Interval slider
interval_label = ctk.CTkLabel(app, text="Interval (seconds):", font=("Arial", 12))
interval_label.pack(pady=(10, 0))

interval_slider = ctk.CTkSlider(app, from_=0.01, to=1.0, command=update_interval)
interval_slider.set(interval)  # Set default value
interval_slider.pack(pady=5)

# Start button
start_button = ctk.CTkButton(app, text="Start Clicking", command=start_clicking_thread)
start_button.pack(pady=(10, 5))

# Stop button
stop_button = ctk.CTkButton(app, text="Stop Clicking", command=stop_clicking)
stop_button.pack(pady=(0, 10))

# Run the application
app.mainloop()
