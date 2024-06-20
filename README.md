# Windows Screen Capture Script

This Python script captures screenshots of your Windows screen every minute for a duration of 2 hours, resulting in 120 screenshots. It uses the `pyautogui` library for taking screenshots and the `time` library to handle the timing.

## Features

- Captures a screenshot every minute.
- Runs for a total duration of 2 hours.
- Saves all screenshots in a specified directory.

## Prerequisites

- Python 3.x
- `pyautogui` library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/screenshots-script.git
    cd screenshots-script
    ```

2. **Install the required library:**

    ```sh
    pip install pyautogui
    ```

## Usage

1. **Run the script:**

    ```sh
    python screenshot_script.py
    ```

2. **The script will:**
    - Create a directory named `screenshots` (if it doesn't exist).
    - Capture a screenshot every minute for 2 hours.
    - Save each screenshot in the `screenshots` directory with a sequential filename (e.g., `screenshot_1.png`, `screenshot_2.png`, etc.).

## Script Details

### `screenshot_script.py`

```python
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
