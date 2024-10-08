from .hotkeys.windows_hotkeys import *
from .hotkeys.chrome_hotkeys import *
from .hotkeys.youtube_hotkeys import *
from .hotkeys.gmail_hotkeys import *

window_aware_gestures = {
    "General": {
        "one": voice_type,
        "peace": notifications_center,
        "three2": file_explorer,
        "four": settings,
        "palm": {"Right": split_right, "Center": screen_capture, "Left": split_left},
        "fist": multi_task,
    },
    "Google Chrome": {
        "YouTube": {"one": full_screen, "peace": next_video},
        "Gmail": {"one": open_starred, "peace": new_mail},
        "one": search_bar,
        "peace": find_in_page,
        "three2": new_tab,
        "four": close_tab,
    },
}
