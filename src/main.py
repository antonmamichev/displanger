import sys
import os
import ctypes
import pyautogui
import tkinter as tk
from PIL import Image, ImageTk

class displanger:

    def __init__(self):

        self.SetDefaults() # Set default values

        self.InitRoot()
        self.CacheLayoutFlags() # Cache the flag images to switch quickly

        self.LaunchEvents() # Start the event loop

    def SetDefaults(self):

        # Map keyboard layouts to flag images
        self.FlagMap = {
            "409": "us.png",  # English (United States)
            "40C": "fr.png",  # French
            "407": "de.png",  # German
            "419": "ru.png",  # Russian
        }

        self.last_layout = None # Track the last detected keyboard layout        
        self.flag_cache = {} # Cache flag images to avoid reloading        
   

    def InitRoot(self):

        # Initialize the Tkinter window
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.attributes("-topmost", True)  # Keep the window on top
        self.root.attributes("-transparentcolor", "white")  # Make the background transparent

        # Create a label to display the flag
        self.flag_label = tk.Label(self.root, bg="white")
        self.flag_label.pack()


    # Launch all events
    def LaunchEvents(self):        

        self.UpdateFlag() # Display the initial flag image
        self.root.mainloop() # Run the Tkinter event loop

    # Get the current keyboard layout
    def GetKeyboardLayout(self):

        user32 = ctypes.WinDLL("user32", use_last_error=True)

        hwnd = user32.GetForegroundWindow()
        thread_id = user32.GetWindowThreadProcessId(hwnd, None)
        layout_id = user32.GetKeyboardLayout(thread_id)

        return hex(layout_id & 0xFFFFFFFF)

    # Cache the flag images for each layout
    def CacheLayoutFlags(self):
        
        root_path = sys._MEIPASS if hasattr(sys, "_MEIPASS") else "src" # Determine the base path for resources
        base_path = os.path.join(root_path, "assets", "flags") # Path to the flag images

        # Cache the flag images for each layout
        for layout, flag_file in self.FlagMap.items():

            flag_path = os.path.join(base_path, flag_file)

            if os.path.exists(flag_path):

                flag_image = Image.open(flag_path)
                self.flag_cache[layout] = ImageTk.PhotoImage(flag_image)

            else:

                print(f"Flag file not found: {flag_path}")

    # Update the flag near the mouse pointer
    def UpdateFlag(self):
        
        layout = self.GetKeyboardLayout()

        layout = str(layout)[-3:]

        # Only update the flag if the layout has changed
        if layout != self.last_layout:
            
            # Update the flag image from the cache
            self.flag_label.config(image=self.flag_cache[layout])
            self.flag_label.image = self.flag_cache[layout]

            self.last_layout = layout

        # Position the flag near the mouse pointer
        x, y = pyautogui.position()
        self.root.geometry(f"+{x+10}+{y+10}")

        # Schedule the next update
        self.root.after(100, self.UpdateFlag)

DL = displanger()