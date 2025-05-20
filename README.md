# 🛑 Web Blocker - Stay Focused During Work Hours

This Python project helps you stay productive by **blocking distracting websites** (like Facebook, Gmail, etc.) during work hours. It modifies the system's `hosts` file to redirect specific URLs to your local machine (`127.0.0.1`), effectively blocking them.
## 📌 Features

- ✅ Automatically blocks websites between **8 AM to 4 PM**
- ✅ Automatically unblocks them after work hours
- ✅ Runs in the background with a 5-second check interval
- ✅ Works on Windows (can be adapted to other OS by changing hosts path)

- 
## 🔍 How It Works

- The script modifies your system's `hosts` file.
- During work hours, it **adds entries** to redirect unwanted domains to `127.0.0.1`.
- After work hours, it **removes those entries**, allowing access again.

## 🖥️ Hosts File Location (Windows)
You can find the `hosts` file on **Windows** here:C:\Windows\System32\drivers\etc\hosts

### 🔎 How to Find It:

1. Open **File Explorer**
2. Navigate to:  
   `C:\Windows\System32\drivers\etc`
3. You may need to enable "Show all files" because the `hosts` file may be hidden or not associated with an app.

---

## ⚠️ Important: Run as Administrator

Since modifying the `hosts` file requires elevated privileges:

- If you're using **VS Code**, open it as Administrator:
  - Right-click the VS Code icon → **Run as administrator**

- If you're using **PyCharm**:
  - Right-click PyCharm → **More** → **Run as administrator**

Otherwise, you will get a `PermissionError` or `FileNotFoundError`.

---
## 🚀 How to Run

1. Open your editor **as Administrator**
2. Ensure Python 3.x is installed
3. Place your script (`main.py`) inside your project folder
4. Update the `hosts_path` in the script if you’re on a different OS
5. Run the script
python main.py


