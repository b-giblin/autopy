import pyautogui
import time

def draw_square(top_left, side_length):
    # Allow some time for the user to switch to a drawing tool
    # (e.g., MS Paint or a similar program)
    print("Starting in 5 seconds...")
    time.sleep(5)

    # Starting position (top-left corner)
    pyautogui.moveTo(top_left)

    # Click to start
    pyautogui.click()

    # Draw square
    for _ in range(4):
        pyautogui.dragRel(side_length, 0, duration=1)  # Move right
        pyautogui.click()
        pyautogui.dragRel(0, side_length, duration=1)  # Move down
        pyautogui.click()
        side_length = -side_length  # Reverse the direction

draw_square((400, 400), 200)  # Start from point (400, 400) with a side length of 200 pixels