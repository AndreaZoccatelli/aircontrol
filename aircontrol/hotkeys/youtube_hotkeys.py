import pyautogui


def full_screen():
    """
    Make video full screen
    """
    pyautogui.press("f")


def next_video():
    """
    Skip to next video
    """
    with pyautogui.hold("shift"):
        pyautogui.press("n")


def pause():
    """
    Pause video
    """
    pyautogui.press("space")
