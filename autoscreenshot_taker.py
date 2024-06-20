# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:34:23 2024

@author: Hp
"""

import pyautogui
import time
import os

# Create a directory to save screenshots if it doesn't exist
save_dir = "screenshots"
os.makedirs(save_dir, exist_ok=True)

# Number of screenshots to take (1 every minute for 2 hours)
num_screenshots = 120
interval = 60  # Interval in seconds (1 minute)

for i in range(num_screenshots):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    # Save the screenshot
    screenshot.save(os.path.join(save_dir, f"screenshot_{i+1}.png"))
    print(f"Screenshot {i+1} taken.")
    # Wait for the next interval
    time.sleep(interval)

print("Screenshot capture completed.")
