from django.db import models
from .validators import validate_cpf, validate_phone

class Person(models.Model):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )

    name = models.CharField(max_length=150)
    phone = models.CharField(
        max_length=13,
        validators=[validate_phone]
    )
    email = models.EmailField()
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
        return self.name