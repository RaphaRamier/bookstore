import re
from validate_docbr import CPF, CNPJ


def name_validate(name):
    return name.isalpha()


def cpf_validate(cpf_number):
    cpf=CPF()
    return cpf.validate(cpf_number)


def cnpj_validate(cnpj_number):
    cnpj=CNPJ()
    return cnpj.validate(cnpj_number)


def phone_validate(phone_number):

    modelo='[0-9]{2} [0-9]{5}-[0-9]{4}'
    response=re.findall(modelo, phone_number)

    return response
