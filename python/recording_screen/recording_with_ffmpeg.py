# -*- encoding: utf-8 -*-
import os, json, time
from datetime import datetime
import sys
import ffmpeg
from PIL import ImageGrab


class recordVideo:
    def __init__(self):
        self.taskParam = {}

    def record_screen(self):
        print("start ffmpeg")

        recording, recordTime = True, 0
        if not os.path.isdir(self.taskParam["file_path"]):
            os.makedirs(self.taskParam["file_path"])

        width = int(self.taskParam["position"]["width"])
        height = int(self.taskParam["position"]["height"])

        t = time.time()
        fps = self.taskParam.get("fps", 30)
        if self.taskParam["allow_record"]:
            # Setup for recording windows desktop to mp4 file
            process = (
                ffmpeg.input(
                    format="gdigrab",
                    framerate=fps,
                    offset_x=0,
                    offset_y=0,
                    filename="desktop",
                    s="{width}x{height}".format(width=width, height=height),
                )
                .output(filename=self.taskParam["fileName"], pix_fmt="yuv420p")
                .overwrite_output()
            )
            # Launch video recording
            process = process.run_async(pipe_stdin=True)
        while (
            self.taskParam["allow_record"] and recordTime < self.taskParam["recordTime"]
        ):
            # print(recordTime)
            recordTime = time.time() - t
        # Stop video recording
        process.communicate(str.encode("q"))
        time.sleep(6)
        # To be sure that the process ends I wait 3 seconds and then terminate de process (wich is more like kill -9)
        process.terminate()
        self.stop()

    def stop(self):
        print("stop record")
        self.taskParam["allow_record"] = False
        time.sleep(4)


if __name__ == "__main__":
    os.chdir(os.path.split(os.path.realpath(__file__))[0])

    screen = ImageGrab.grab()
    width, height = screen.size
    del screen

    taskjson = {
        "result": "true",
        "data": {
            "id": "1",
            "duration": 60,
            "width": width,
            "recordUrl": "Example Domain",
            "height": height,
            "bitrate": "1024k",
        },
    }

    record = recordVideo()
    record.taskParam["position"] = {}
    record.taskParam["position"]["width"] = taskjson["data"]["width"]
    record.taskParam["position"]["height"] = taskjson["data"]["height"]
    record.taskParam["allow_record"] = True
    record.taskParam["recordTime"] = int(taskjson["data"]["duration"])
    record.taskParam["file_path"] = os.path.join(".")
    record.taskParam["timeStamp"] = str(int(time.time() * 1e3))
    record.taskParam["fileName"] = os.path.join(
        record.taskParam["file_path"], record.taskParam["timeStamp"] + ".mp4"
    )
    record.taskParam["bitrate"] = taskjson["data"]["bitrate"]
    record.taskParam["recordId"] = taskjson["data"]["id"]
    record.record_screen()
