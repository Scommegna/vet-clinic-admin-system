from django.db import models
from person.models import Person
from .validators import validate_crmv

class Vet(Person):
    crmv = models.CharField(
        max_length=8,
        unique=True,
        validators=[validate_crmv],
        help_text="Enter in the format UF12345 (e.g., MG12345)"
    )
    specialty = models.CharField(max_length=100)


    def _str_(self):
        return f"{self.name} ({self.crmv})"