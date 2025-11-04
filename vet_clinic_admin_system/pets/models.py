from django.db import models
from person.models import Person

class Pet(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('rodent', 'Rodent'),
        ('other', 'Other'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    WEIGHT_UNIT_CHOICES = [
        ("kg", "Kilogram"),
        ("g", "Gram"),
    ]

    HEIGHT_UNIT_CHOICES = [
        ("cm", "Centimeter"),
        ("m", "Meter"),
    ]

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="pets"
    )

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    weight = models.FloatField()
    weight_unit = models.CharField(
        max_length=2,
        choices=WEIGHT_UNIT_CHOICES,
        default="kg"
    )

    height = models.FloatField()
    height_unit = models.CharField(
        max_length=2,
        choices=HEIGHT_UNIT_CHOICES,
        default="cm"
    )

    birth_date = models.DateField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
