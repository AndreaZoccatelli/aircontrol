import pyautogui
import time

def screen_capture():
    pyautogui.hotkey("win", "shift", "s")

def split_right():
    with pyautogui.hold('win'):
        pyautogui.press('right')
    time.sleep(0.8)
    pyautogui.press('enter')

def split_left():
    with pyautogui.hold('win'):
        pyautogui.press('left')
    time.sleep(0.8)
    pyautogui.press('enter')

def voice_type():
    with pyautogui.hold("win"):
        pyautogui.press("h")

def multi_task():
    with pyautogui.hold("win"):
        pyautogui.press("tab")
    
