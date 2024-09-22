import pyautogui


def close_tab():
    """
    Close current Chrome tab
    """
    with pyautogui.hold("ctrl"):
        pyautogui.press("w")


def find_in_page():
    """
    Find word in web page
    """
    with pyautogui.hold("ctrl"):
        pyautogui.press("f")


def new_tab():
    """
    Open new Chrome tab
    """
    with pyautogui.hold("ctrl"):
        pyautogui.press("t")


def new_window():
    """
    Open new Chrome window
    """
    with pyautogui.hold("ctrl"):
        pyautogui.press("n")


def search_bar():
    """
    Jump to search bar
    """
    with pyautogui.hold("ctrl"):
        pyautogui.press("l")
    pyautogui.press("backspace")


def to_last_tab():
    """
    Go to last Chrome tab
    """
    with pyautogui.hold("ctrl"):
        pyautogui.press("9")
