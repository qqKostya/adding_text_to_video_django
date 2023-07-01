import time
from django.http import HttpResponse
from django.shortcuts import render
from .utils.video_generator import generate_video

def generate_video_view(request):
    text = request.GET.get('text', '')
    output_path = 'media/videos/'
    generate_video(text, output_path)

    video_number = int(time.time())
    video_filename = f"running_text{video_number}.avi"

    with open(output_path + video_filename, 'rb') as f:
        response = HttpResponse(f.read(), content_type='video/avi')
        response['Content-Disposition'] = 'attachment; filename=' + video_filename
        return response
