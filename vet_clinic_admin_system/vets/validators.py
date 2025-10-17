import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_crmv(value: str):
    pattern = r'^[A-Z]{2}\d{1,6}$'
    if not re.match(pattern, value):
        raise ValidationError(
            _(f"'{value}' is not a valid CRMV. Use the format: ‘UF12345’ (e.g., MG12345)")
        )