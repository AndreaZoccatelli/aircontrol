import mediapipe as mp
from mediapipe.tasks import python
import os

BaseOptions = python.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
model_path = r"aircontrol\models\gesture_recognizer_zoom_full.task"
