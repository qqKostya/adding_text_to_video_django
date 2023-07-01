from django.urls import path
from . import views

app_name = 'video_generator'

urlpatterns = [
    path('generate/', views.generate_video_view, name='generate'),
]
