from flask import Flask, render_template
import subprocess
import os
import pyautogui
import time

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start_detection():
    script_path = os.path.abspath("live_detection.py")
    subprocess.Popen(["python", script_path],creationflags=subprocess.CREATE_NO_WINDOW)  # Hide CMD
    time.sleep(2)  # Give time for the window to open
    pyautogui.hotkey('alt', 'tab')  # Bring it to the front
    return "Live Detection Started!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)