from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
    
class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class GolfLocation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TrainingType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="bookings")
    class_date = models.DateTimeField(null=False)
    location = models.ForeignKey(GolfLocation, on_delete=models.DO_NOTHING, related_name="locations")
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING, related_name="trainers")
    training_type = models.ForeignKey(TrainingType, on_delete=models.DO_NOTHING, related_name="trainers")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.class_date}"

class Booking2(models.Model):
    user = models.CharField(max_length=500)
    class_date = models.DateTimeField(null=False)
    location = models.CharField(max_length=500)
    trainer = models.CharField(max_length=500)
    training_type = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"