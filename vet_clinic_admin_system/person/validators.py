from django.core.exceptions import ValidationError
import re

def validate_cpf(value: str):
    cpf = re.sub(r"[^0-9]", "", value)

    if len(cpf) != 11:
        raise ValidationError("CPF must have 11 digits.")

    if cpf == cpf[0] * 11:
        raise ValidationError("Invalid CPF.")

    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            raise ValidationError("Invalid CPF.")

def validate_phone(value: str):
    phone_regex = r"^55\d{10,11}$"
    if not re.match(phone_regex, value):
        raise ValidationError(
            "Phone number must respect the format 55<DDD><number>, ex: 5511998765432"
        )