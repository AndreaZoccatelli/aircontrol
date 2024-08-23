import pyautogui

def full_screen():
    pyautogui.press("f")

def pause():
    pyautogui.press("space")

def next_video():
    with pyautogui.hold('shift'):
        pyautogui.press('n')