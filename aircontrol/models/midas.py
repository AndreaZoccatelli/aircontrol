import torch
import cv2 as cv
import numpy as np


class MidasModel:
    """
    Class to load Intel MiDaS model and make predictions
    """

    def __init__(self, model: str = "DPT_Hybrid") -> None:
        """
        Args:
            model (str): MiDaS model version, available options are ["MiDaS_small", "DPT_Hybrid", "DPT_Large"]. Defaults to "DPT_Hybrid".

        Raises:
            ValueError: if model is not one of ["MiDaS_small", "DPT_Hybrid", "DPT_Large"]
        """
        if model not in ["MiDaS_small", "DPT_Hybrid", "DPT_Large"]:
            raise ValueError(
                "Available models are ['MiDaS_small', 'DPT_Hybrid', 'DPT_Large']"
            )
        self.midas = torch.hub.load("intel-isl/MiDaS", model)
        self.device = (
            torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        )
        self.midas.to(self.device)
        transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
        self.transform = transforms.small_transform

    def predict_adjust(self, frame: np.ndarray) -> np.ndarray:
        """
        Args:
            frame (np.ndarray): frame captured by webcam

        Returns:
            np.ndarray: depth map of the frame
        """
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
        adjusted_frame = frame * output_norm[:, :, np.newaxis]
        adjusted_frame = adjusted_frame.astype(np.uint8)
        return adjusted_frame
