import multiprocessing
import threading
import time
from pathlib import Path
from typing import Dict

import cv2
import numpy as np
from PIL import ImageGrab


@profile
def start_recording(event: threading.Event, save_path: Path, frame: int):
    _frame = 20
    fourcc = cv2.VideoWriter_fourcc("X", "V", "I", "D")
    screen = ImageGrab.grab()
    width, high = screen.size
    del screen
    _video_writer = cv2.VideoWriter(
        str(save_path.absolute()), fourcc, _frame, (width, high)
    )
    while True:
        try:
            if event.is_set():
                _video_writer.release()
                print(f"Recording finished, {save_path}")
                break

            # 图片为RGB模式
            img = ImageGrab.grab()
            # 转为opencv的BGR模式
            bgr_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            _video_writer.write(bgr_img)
        except Exception as e:
            print(f"----> Recording failed, since {e}")
        finally:
            time.sleep(1 / frame)
            # time.sleep(0.001)


class ScreenRecorder:
    def __init__(
        self, end_signal_queue: multiprocessing.Queue, save_path: Path, frame: int
    ):
        self.end_signal_queue = end_signal_queue
        self.event = threading.Event()
        self.recording_thread = threading.Thread(
            target=start_recording, args=(self.event, save_path, frame)
        )

    def start(self):
        self.recording_thread.start()
        while True:
            signal = self.end_signal_queue.get()
            self.event.set()
            print(f"Send end recording signal")
            time.sleep(1)
            break


def recording_process(
    end_signal_queue: multiprocessing.Queue, save_path: Path, frame: int
):
    recorder = ScreenRecorder(end_signal_queue, save_path, frame)
    recorder.start()


class VideoRecorder:
    def __init__(self, config: Dict):
        self.end_signal_queue = multiprocessing.Queue()
        self.enable = config.get("enable", False)
        self.save_path = (
            Path(config.get("video_path")) if config.get("video_path") else None
        )
        self.frame = config.get("frame", 50)

    def start(self):
        if self.enable:
            print(f"Start recording to {self.save_path}")
            process = multiprocessing.Process(
                target=recording_process,
                args=(self.end_signal_queue, self.save_path, self.frame),
            )

            process.start()

    def end(self):
        if self.enable:
            self.end_signal_queue.put("end")


if __name__ == "__main__":
    recorder = VideoRecorder(
        config={
            "enable": True,
            "video_path": "recording.avi",
        }
    )

    recorder.start()
    print("record starting")

    time.sleep(60)

    recorder.end()
    print("record end")
