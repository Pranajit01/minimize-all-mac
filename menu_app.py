import json
from pathlib import Path

import rumps
from pynput import keyboard

from minimize_all import minimize_all


CONFIG_FILE = Path(__file__).with_name("config.json")

DEFAULT_CONFIG = {
    "shortcut": "<ctrl>+<alt>+d"
}


def load_config():
    try:
        if CONFIG_FILE.exists():
            config = json.loads(CONFIG_FILE.read_text())
            shortcut = config.get(
                "shortcut",
                DEFAULT_CONFIG["shortcut"]
            )

            if isinstance(shortcut, str) and shortcut.strip():
                return shortcut

    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not read configuration: {error}")

    return DEFAULT_CONFIG["shortcut"]


class MinimizeAllApp(rumps.App):

    def __init__(self):
        super().__init__(
            "Minimize",
            title="⇲",
            menu=[
                "Minimize All Windows",
                None,
                "Show Shortcut",
                None,
                "Quit"
            ]
        )

        self.shortcut = load_config()

        self.hotkey_listener = keyboard.GlobalHotKeys({
            self.shortcut: self.minimize_windows
        })

        self.hotkey_listener.start()

        print("Minimize All menu-bar app started.")
        print(f"Global shortcut: {self.shortcut}")

    @rumps.clicked("Minimize All Windows")
    def minimize_windows(self, _=None):
        minimize_all()

    @rumps.clicked("Show Shortcut")
    def show_shortcut(self, _):
        rumps.alert(
            title="Minimize All",
            message=f"Your shortcut is:\n{self.shortcut}"
        )

    @rumps.clicked("Quit")
    def quit_app(self, _):
        self.hotkey_listener.stop()
        rumps.quit_application()


if __name__ == "__main__":
    app = MinimizeAllApp()
    app.run()