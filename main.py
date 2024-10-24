import pyautogui
import threading
import time
import keyboard  # Import the keyboard library
from pynput.mouse import Listener
import cv2
import numpy as np
from PIL import Image

tiles_position = []
click_count = 0

def on_click(x, y, button, pressed):
    global click_count
    
    # Check if the click is a right-click and if the button is pressed down
    if pressed and button == button.right:
        click_count += 1
        print(f"Right mouse clicked at ({x}, {y})")
        tiles_position.append((x, y))
        
        # Stop listener after 4 right-clicks
        if click_count >= 4:
            return False  # This stops the listener

# Set up the listener
with Listener(on_click=on_click) as listener:
    listener.join()

print(tiles_position)




# Load the saved image you want to search for
template_path = "start.png"  # Replace with your image path
template = cv2.imread(template_path, cv2.IMREAD_COLOR)

# Take a screenshot and convert it to an OpenCV image
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Get the dimensions of the template image
w, h = template.shape[1], template.shape[0]

# Perform template matching
result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Define a threshold for matching accuracy (adjust if necessary)
threshold = 0.8  # 80% matching

if max_val >= threshold:
    print(f"Image found at location: {max_loc}")
    x_start, y_start = max_loc
    print(f"Top-left corner of the found image: ({x_start}, {y_start})")
else:
    print("Image not found.")

pyautogui.click(x_start,y_start)


pyautogui.FAILSAFE = False

# Define the search functions
def search1():
    pixel_color = pyautogui.pixel(tiles_position[0][0], tiles_position[0][1])
    r,g,b=pixel_color
    print(f"The RGB value at (1360, 500) is: {r,g,b}")
    if r==0 and g==0 and b==0:
        pyautogui.click(tiles_position[0][0], tiles_position[0][1])
def search2():
    pixel_color = pyautogui.pixel(tiles_position[1][0], tiles_position[1][1])
    r,g,b=pixel_color
    print(f"The RGB value at (1560, 500) is: {r,g,b}")
    if r==0 and g==0 and b==0:
        pyautogui.click(tiles_position[1][0], tiles_position[1][1])
def search3():
    pixel_color = pyautogui.pixel(tiles_position[2][0], tiles_position[2][1])
    r,g,b=pixel_color
    print(f"The RGB value at (1660, 500) is: {r,g,b}")
    if r==0 and g==0 and b==0:
        pyautogui.click(tiles_position[2][0], tiles_position[2][1])
def search4():
    pixel_color = pyautogui.pixel(tiles_position[3][0], tiles_position[3][1])
    r,g,b=pixel_color
    print(f"The RGB value at (1860, 500) is: {r,g,b}")
    if r==0 and g==0 and b==0:
        pyautogui.click(tiles_position[3][0], tiles_position[3][1])

# Create a list to hold threads
threads = []
while not keyboard.is_pressed('q'):  # Loop while 'q' is not pressed
    for search_function in (search1, search2, search3, search4):
        t = threading.Thread(target=search_function)
        threads.append(t)
        t.start()  # Start the thread immediately
    # Wait for all threads to complete
    for t in threads:
        t.join()




print("All searches completed.")
