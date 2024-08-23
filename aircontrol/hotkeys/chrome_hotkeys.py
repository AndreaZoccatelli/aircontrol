import pyautogui

def search_bar():
    with pyautogui.hold("ctrl"):
        pyautogui.press("l")
    pyautogui.press("backspace")

def new_window():
    with pyautogui.hold("ctrl"):
        pyautogui.press("n")

def new_tab():
    with pyautogui.hold("ctrl"):
        pyautogui.press("t")

def close_tab():
    with pyautogui.hold("ctrl"):
        pyautogui.press("w")

def to_last_tab():
    with pyautogui.hold("ctrl"):
        pyautogui.press("9")

def find_in_page():
    with pyautogui.hold("ctrl"):
        pyautogui.press("f")     