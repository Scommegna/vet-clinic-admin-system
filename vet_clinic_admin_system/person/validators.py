from django.core.exceptions import ValidationError
import re

def validate_cpf(value: str):
    cpf = re.sub(r"[^0-9]", "", value)

    if len(cpf) != 11:
        raise ValidationError("O CPF deve conter 11 dígitos.")

    if cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido.")

    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            raise ValidationError("CPF inválido.")

def validate_phone(value: str):
    phone_regex = r"^55\d{10,11}$"
    if not re.match(phone_regex, value):
        raise ValidationError(
            "O telefone deve estar no formato 55<DDD><número>, ex: 5511998765432"
        )