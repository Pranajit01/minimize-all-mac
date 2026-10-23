import json
from pathlib import Path
from pynput import keyboard
from minimize_all import minimize_all

CONFIG_FILE = Path(__file__).with_name("config.json")

DEFAULT_CONFIG = {
    "shortcut": "<ctrl>+<alt>+d"
}


def load_config():
    if not CONFIG_FILE.exists():
        CONFIG_FILE.write_text(
            json.dumps(DEFAULT_CONFIG, indent=4)
        )

    try:
        return json.loads(CONFIG_FILE.read_text())
    except (json.JSONDecodeError, OSError):
        print("Invalid configuration. Using the default shortcut.")
        return DEFAULT_CONFIG


config = load_config()
shortcut = config.get("shortcut", DEFAULT_CONFIG["shortcut"])

print("Minimize All is running.")
print(f"Shortcut: {shortcut}")
print("Press Ctrl+C in Terminal to quit.")

with keyboard.GlobalHotKeys({
    shortcut: minimize_all
}) as listener:
    listener.join()