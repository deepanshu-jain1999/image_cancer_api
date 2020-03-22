from rest_framework import serializers
from .models import Media


class MediaSerializer(serializers.ModelSerializer):
    web_opinion = serializers.ReadOnlyField()

    class Meta:
        model = Media
        fields = '__all__'
