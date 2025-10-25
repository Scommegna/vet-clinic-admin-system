from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_cpf, validate_phone

class Person(AbstractUser):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )

    phone = models.CharField(
        max_length=13,
        validators=[validate_phone],
        unique=True
    )
    document = models.CharField(
        max_length=11,
        validators=[validate_cpf],
        unique=True,
        help_text="Enter the CPF with or without punctuation."
    )
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username or self.email