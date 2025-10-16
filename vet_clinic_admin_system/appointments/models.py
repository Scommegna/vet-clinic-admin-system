from django.db import models
from pets.models import Pet
from vets.models import Vet


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="appointments")
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, related_name="appointments")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    datetime = models.DateTimeField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Appointment for {self.pet.name} with Dr. {self.vet.name} on {self.datetime.strftime('%Y-%m-%d %H:%M:%S')}"