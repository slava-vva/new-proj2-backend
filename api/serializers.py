from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note, Trainer, TrainingType, GolfLocation, Booking, Booking2

class Booking2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Booking2
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Booking
        fields = '__all__'
    #class_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S", input_formats=["%Y-%m-%dT%H:%M", "%Y-%m-%dT%H:%M:%S"])
    #user = serializers.StringRelatedField(read_only=True)  # Shows username instead of ID

class GolfLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GolfLocation
        fields = '__all__'

class TrainingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingType
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}


