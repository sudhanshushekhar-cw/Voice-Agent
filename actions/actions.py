from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pyautogui
import subprocess
import os
from send2trash import send2trash

# --- Close Tab ---
class ActionCloseTab(Action):
    def name(self):
        return "action_close_tab"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        pyautogui.hotkey('ctrl', 'w')
        dispatcher.utter_message(text="Tab closed ✅")
        return []

# --- Open Notepad ---
class ActionOpenNotepad(Action):
    def name(self):
        return "action_open_notepad"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        subprocess.Popen("notepad.exe")
        dispatcher.utter_message(text="Notepad opened ✅")
        return []

# --- Open Browser ---
class ActionOpenBrowser(Action):
    def name(self):
        return "action_open_browser"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        import webbrowser
        webbrowser.open("https://www.google.com")
        dispatcher.utter_message(text="Browser opened ✅")
        return []

# --- Delete File to Recycle Bin ---
class ActionDeleteFile(Action):
    def name(self):
        return "action_delete_file"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        file_name = next(tracker.get_latest_entity_values("file"), None)
        if file_name:
            path = os.path.abspath(os.path.expanduser(file_name))
            if os.path.exists(path):
                send2trash(path)
                dispatcher.utter_message(text=f"{file_name} moved to Recycle Bin ✅")
            else:
                dispatcher.utter_message(text="File not found ❌")
        else:
            dispatcher.utter_message(text="File name missing ❌")
        return []
