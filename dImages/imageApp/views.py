from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from imageApp.serializers import ImageSerializer


class UploadImagesView(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        serialized_image = ImageSerializer(data=request.data)
        if serialized_image.is_valid():
            serialized_image.save()
            return Response(serialized_image.data, status=status.HTTP_201_CREATED)
        return Response(serialized_image.errors, status=status.HTTP_400_BAD_REQUEST)
