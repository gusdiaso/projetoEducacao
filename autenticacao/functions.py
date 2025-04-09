from django.forms import ValidationError
from django.conf import settings


from django.core.exceptions import ValidationError

def validate_cpf(cpf):
    """
    Function that validates a CPF.
    """
    cpf = cpf.strip().replace('.', '').replace('-', '')
    
    if not cpf.isdigit():
        raise ValidationError('O CPF deve conter apenas números.', code='invalid1')

    if len(cpf) != 11:
        raise ValidationError('O CPF deve conter 11 dígitos.', code='invalid1')

    if cpf in [c * 11 for c in "0123456789"]:
        raise ValidationError('CPF inválido.', code='invalid2')

    # Primeiro dígito verificador
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    check_digit1 = 11 - (total % 11)
    if check_digit1 > 9:
        check_digit1 = 0
    if check_digit1 != int(cpf[9]):
        raise ValidationError('CPF inválido.', code='invalid2')

    # Segundo dígito verificador
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    check_digit2 = 11 - (total % 11)
    if check_digit2 > 9:
        check_digit2 = 0
    if check_digit2 != int(cpf[10]):
        raise ValidationError('CPF inválido.', code='invalid2')

    return cpf
