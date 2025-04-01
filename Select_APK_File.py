import tkinter as tk
from tkinter import filedialog
import os

def select_apk_file():
    """Opens a file dialog to select an APK file and returns its path.

    Returns:
        str: The absolute path to the selected APK file, or an empty string
             if no file was selected or the dialog was closed.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select APK File",
        filetypes=[("APK files", "*.apk")]
    )

    return file_path

if __name__ == "__main__":
    apk_path = select_apk_file()

    if apk_path:
        print(f"Selected APK file: {apk_path}")
        # You can now work with the selected APK file path, for example:
        # print(f"File name: {os.path.basename(apk_path)}")
        # print(f"File directory: {os.path.dirname(apk_path)}")
    else:
        print("No APK file selected.")
