import pyautogui
import time


def file_explorer():
    """
    Open file explorer
    """
    pyautogui.hotkey("win", "e")


def multi_task():
    """
    Open Windows multi-tasking
    """
    with pyautogui.hold("win"):
        pyautogui.press("tab")


def notifications_center():
    """
    Open notifications center
    """
    pyautogui.hotkey("win", "a")


def screen_capture():
    """
    Open screenshot tool
    """
    pyautogui.hotkey("win", "shift", "s")


def settings():
    """
    Open settings
    """
    pyautogui.hotkey("win", "i")


def split_left():
    """
    Split current window to the left-side of the screen
    """
    with pyautogui.hold("win"):
        pyautogui.press("left")


def split_right():
    """
    Split current window to the right-side of the screen
    """
    with pyautogui.hold("win"):
        pyautogui.press("right")


def voice_type():
    """
    Start voice typing
    """
    with pyautogui.hold("win"):
        pyautogui.press("h")
