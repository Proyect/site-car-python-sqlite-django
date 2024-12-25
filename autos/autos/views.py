from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vehicle, Img, Description
from .serializers import AutoSerializer, ImgSerializer, DescriptionSerializer

class AutoAPIView(APIView):
    def get(self, request):
        autos = Vehicle.objects.all()
        serializer = AutoSerializer(autos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImgAPIView(APIView):
    def get(self, request):
        imagenes = Img.objects.all()
        serializer = ImgSerializer(imagenes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DescriptionAPIView(APIView):
    def get(self, request):
        publicaciones = Description.objects.all()
        serializer = DescriptionSerializer(publicaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
