import cv2
import numpy as np
import time


def generate_video(text, output_path):
    width, height = 100, 100
    fps = 30
    duration = 3

    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    video_number = int(time.time())
    video_name = output_path + f"running_text{video_number}.avi"
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    x = width
    y = height // 2

    text_color = (255, 255, 255)
    background_color = (0, 255, 0)


    text_length = len(text)
    speed = int((width + text_length * text_length) / (duration * fps))
    if speed == 0:
        speed = 1

    for _ in range(duration * fps):
        frame = np.full((height, width, 3), background_color, dtype=np.uint8)

        

        cv2.putText(
            frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2, cv2.LINE_AA
        )
        video.write(frame)
        x -= speed

    video.release()
