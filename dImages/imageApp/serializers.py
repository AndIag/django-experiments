from rest_framework import serializers

from imageApp.models import StdImage


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    class Meta:
        model = StdImage
        fields = ('id', 'image')
        read_only_fields = ('id',)
