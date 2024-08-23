import pyautogui

def new_mail():
    pyautogui.press('c')

def open_starred():
    with pyautogui.hold('g'):
        pyautogui.press('s')

def open_sent():
    with pyautogui.hold('g'):
        pyautogui.press('t')

def open_drafts():
    with pyautogui.hold('g'):
        pyautogui.press('d')