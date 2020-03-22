from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Media
from .serializers import MediaSerializer


class MediaViewset(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    def perform_create(self, serializer):
        skin_image = serializer.validated_data['skin_image']
        result = "pending"
        serializer.save(web_opinion=result)
        return Response(result, status.HTTP_201_CREATED)
