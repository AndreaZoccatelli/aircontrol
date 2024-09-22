import pyautogui


def new_mail():
    """
    Open tab to write a new email
    """
    pyautogui.press("c")


def open_drafts():
    """
    Open draft emails
    """
    with pyautogui.hold("g"):
        pyautogui.press("d")


def open_sent():
    """
    Open sent emails tab
    """
    with pyautogui.hold("g"):
        pyautogui.press("t")


def open_starred():
    """
    Open starred emails tab
    """
    with pyautogui.hold("g"):
        pyautogui.press("s")
