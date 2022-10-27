
from rest_framework import viewsets

from video.models import Video
from video.serializer import VideoSerializer
class VideoViewSet(viewsets.ModelViewSet):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer
