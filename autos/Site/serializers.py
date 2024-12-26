from rest_framework import serializers
from .models import Vehicle, Img,  Description

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = '__all__'
        
class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'