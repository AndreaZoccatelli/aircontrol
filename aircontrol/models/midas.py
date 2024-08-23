import torch
import cv2 as cv
import numpy as np


class MidasModel:
    def __init__(self) -> None:
        self.midas = torch.hub.load("intel-isl/MiDaS", "DPT_Hybrid")
        self.device = (
            torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        )
        self.midas.to(self.device)
        transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
        self.transform = transforms.small_transform

    def predict_adjust(self, frame):
        imgbatch = self.transform(frame).to(self.device)
        with torch.no_grad():
            prediction = self.midas(imgbatch)
            prediction = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=frame.shape[:2],
                mode="bicubic",
                align_corners=False,
            ).squeeze()

        output = prediction.cpu().numpy()
        # Normalizing the output predictions for cv2 to read.
        output_norm = cv.normalize(
            output, None, 0, 1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F
        )
        frame = frame.astype(np.float32) / 255.0
        adjusted_frame = np.clip(frame * output_norm[:, :, np.newaxis], 0, 1)
        adjusted_frame = (adjusted_frame * 255).astype(np.uint8)
        return adjusted_frame
