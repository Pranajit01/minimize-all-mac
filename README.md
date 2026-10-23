# Minimize All Mac ⇲

A lightweight macOS menu bar utility that minimizes all open application windows all at once.

On macOS, there is no single default shortcut to minimize all open windows into the Dock. This app adds that feature with a global keyboard shortcut and a menu bar icon.

---

## 💡 About The Project

If you have ever moved from Windows (`Win + D`) to macOS, or simply work with dozens of open windows across browsers, code editors, and communication apps, you have likely noticed that macOS lacks a native shortcut to minimize everything at once:

- **Show Desktop (`Fn + F11` / Trackpad gesture)**: Only temporarily slides windows to the screen edges. The moment you interact with any app, all the clutter snaps right back.
- **`Cmd + Option + M`**: Only minimizes windows for the *single foreground app* you are currently focused on, leaving all background apps untouched.

**Minimize All Mac** provides the missing feature:

With one global shortcut (**`Control + Option + D`**) or a single click from the menu bar icon (**`⇲`**), it cleanly minimizes every visible application window directly into your Dock, giving you a fresh, distraction-free workspace in an instant.

---

## 📥 Option 1: Download & Install (No Terminal Required)

1. Download **`Minimize-All-Mac.zip`** from the [Releases](https://github.com/Pranajit01/minimize-all-mac/releases) tab.
2. Unzip it and drag **`Minimize All.app`** into your **Applications** folder.
3. Double-click to open.

### ⚠️ First-Time Setup (Required macOS Permissions)

Because macOS protects window controls and keyboard shortcuts, you need to allow permission once:

1. **Gatekeeper Notice**:
   - On the first open, macOS may show a prompt saying the app is from an unidentified developer.
   - **Right-click (or Control-click)** `Minimize All.app` in your Applications folder and select **Open**, then click **Open**.
2. **Accessibility Permission**:
   - Go to **System Settings** > **Privacy & Security** > **Accessibility**.
   - Turn the toggle **ON** for **Minimize All**.

---

## ⌨️ How to Use

- **Default Shortcut**: Press `Control` + `Option` + `D` from anywhere to minimize all windows.
- **Menu Bar Icon**: Click the **⇲** icon in the top macOS menu bar and select **Minimize All Windows**.

---

## ⚙️ How to Customize Your Shortcut

The shortcut is configured in `config.json`:

```json
{
  "shortcut": "<ctrl>+<alt>+d"
}
```

To change it:
1. Open `config.json` in any text editor (such as TextEdit).
2. Change the key combination to your preferred keys.
   - Example for Command + Option + M: `"<cmd>+<alt>+m"`
   - Example for Control + Option + H: `"<ctrl>+<alt>+h"`
3. Save the file and restart the app.

---

## 🛠️ Option 2: Build the App on Your Own

If you want to run from source or build the `.app` bundle yourself:

### 1. Requirements
- macOS
- Python 3.10 or higher

### 2. Setup
```bash
# Clone the repository
git clone https://github.com/Pranajit01/minimize-all-mac.git
cd minimize-all-mac

# Create virtual environment and install packages
python3 -m venv .venv
source .venv/bin/activate
pip install rumps pynput pyinstaller
```

### 3. Run the App
```bash
python menu_app.py
```

### 4. Build the Standalone `.app`
```bash
pyinstaller "Minimize All.spec"
```
The finished application bundle will be created inside the `dist/` folder:
`dist/Minimize All.app`

---

## 🚀 Launch Automatically on Startup (Optional)

1. Open **System Settings** > **General** > **Login Items**.
2. Under **Open at Login**, click the **+** button.
3. Select **Minimize All** from your **Applications** folder.
