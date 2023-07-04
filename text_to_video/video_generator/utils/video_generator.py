from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import time
import os


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

    font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Roboto-Regular.ttf")
    font_size = 20
    font = ImageFont.truetype(font_path, font_size)

    for _ in range(duration * fps):
        frame = np.full((height, width, 3), background_color, dtype=np.uint8)
        img_pil = Image.fromarray(frame)
        draw = ImageDraw.Draw(img_pil)
        draw.text((x, y), text, font=font, fill=text_color)
        frame = np.array(img_pil)

        video.write(frame)
        x -= speed

    video.release()
