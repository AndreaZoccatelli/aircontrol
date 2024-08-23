import ctypes
import pyautogui

def numlock_off():
    if ctypes.windll.user32.GetKeyState(0x90) & 1:
        pyautogui.press('numlock')

def get_window():
    window_title=pyautogui.getActiveWindowTitle()
    window_title=window_title.split(' - ')
    window=window_title[-1]
    sub_window=window_title[-2]
    return window, sub_window

