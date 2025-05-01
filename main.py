import tkinter as tk
import keyboard
import threading

# Counters and UI labels
counters = []
labels = []

# GUI setup
root = tk.Tk()
root.attributes('-topmost', True)
root.overrideredirect(True)
root.wm_attributes('-transparentcolor', 'white')
root.configure(bg='white')
root.geometry('+50+50')  # Optional: screen position

frame = tk.Frame(root, bg='white')
frame.pack()

def update_display():
    for label in labels:
        label.destroy()
    labels.clear()
    for count in counters:
        label = tk.Label(frame, text=str(count), font=("Arial", 18), fg="black", bg="white")
        label.pack(anchor='w')
        labels.append(label)

def add_counter():
    counters.append(0)
    root.after(0, update_display)

def increment_latest():
    if counters:
        counters[-1] += 1
        root.after(0, update_display)

def delete_latest():
    if counters:
        counters.pop()
        root.after(0, update_display)

def exit_app():
    print("Exiting...")
    root.quit()

def keyboard_listener():
    keyboard.add_hotkey('ctrl+shift+n+l', add_counter)
    keyboard.add_hotkey('ctrl+shift+k', increment_latest)
    keyboard.add_hotkey('ctrl+shift+x', delete_latest)
    keyboard.add_hotkey('ctrl+shift+q', exit_app)  # Optional exit shortcut
    keyboard.wait()  # keep thread alive

# Start keyboard listener in background thread
keyboard_thread = threading.Thread(target=keyboard_listener, daemon=True)
keyboard_thread.start()

# Start GUI in main thread
root.mainloop()
