from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'trainers', views.TrainerViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'bookings2', views.Booking2ViewSet)
router.register(r'golflocations', views.GolfLocationViewSet)
router.register(r'trainingtype', views.TrainingTypeViewSet)

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
    path('', include(router.urls)),
]