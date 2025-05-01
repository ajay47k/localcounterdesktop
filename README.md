Here's a clean and "pyara sa" `README.md` for your transparent on-screen counter tool:

---

## 🧮 On-Screen Transparent Counter

A lightweight, always-on-top, translucent counter tool built with Python and Tkinter. Control it globally using keyboard shortcuts! Perfect for productivity tracking, live event counting, or anything you want to tally without switching windows.

---

### ✨ Features

✅ Transparent floating window  
✅ Always stays on top  
✅ Create multiple counters  
✅ Global keyboard shortcuts (even when not focused)  
✅ Minimal, distraction-free display  
✅ Fully customizable

---

### ⚙️ Requirements

- Python 3.7+
- `keyboard` library  
  Install via pip:

```bash
pip install keyboard
```

---

### 🚀 How to Run

1. Save the Python script as `counter.py`.
2. Run it as **Administrator** (important for global hotkeys on Windows):

```bash
python counter.py
```

---

### 🎮 Hotkeys (Global)

| Shortcut              | Action                         |
|-----------------------|--------------------------------|
| `Ctrl + Shift + N + L`| Add a new counter              |
| `Ctrl + Shift + K`    | Increment the latest counter   |
| `Ctrl + Shift + X`    | Delete the latest counter      |
| `Ctrl + Shift + Q`    | Exit the application           |

> ⚠️ Use **rare key combinations** to avoid conflicts with other apps.

---

### 📌 Notes

- The window is draggable only via code customization.
- You can customize font, position, and colors easily in the script.
- Avoid using hotkey combos that are already reserved by system or other apps.
- On first run, Windows Defender or antivirus may flag it due to global key hooks. This is normal — allow if you trust the script.

---

### 🧠 Custom Ideas

Want to extend it? Here are some suggestions:
- Named counters
- Save/load counter state
- Draggable UI
- Custom shortcut editor
- Sound/notification when count increases

---

Made with 🐍 and ☕ by [Ajay Sengar](mailto:asengar@umd.edu)
