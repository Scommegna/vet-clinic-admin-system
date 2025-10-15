import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_crmv(value: str):
    pattern = r'^[A-Z]{2}\d{1,6}$'
    if not re.match(pattern, value):
        raise ValidationError(
            _(f"'{value}' não é um CRMV válido. Use o formato: 'UF12345' (ex.: MG12345)")
        )