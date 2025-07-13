from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from .serializers import UserSerializer, NoteSerializer, TrainerSerializer, BookingSerializer, GolfLocationSerializer, TrainingTypeSerializer, Booking2Serializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note, Trainer, Booking, GolfLocation, TrainingType, Booking2

class GolfLocationViewSet(viewsets.ModelViewSet):
    queryset = GolfLocation.objects.all()
    serializer_class = GolfLocationSerializer
    permission_classes = [AllowAny]

class TrainingTypeViewSet(viewsets.ModelViewSet):
    queryset = TrainingType.objects.all()
    serializer_class = TrainingTypeSerializer
    permission_classes = [AllowAny]

class Booking2ViewSet(viewsets.ModelViewSet):
    queryset = Booking2.objects.all()
    serializer_class = Booking2Serializer
    permission_classes = [AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

    #def perform_create(self, serializer):
    #    serializer.save(user=self.request.user)  # Set current user automatically

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [AllowAny]

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]