def soma_10(x):
    return x + 10


def pagamento(qtd_horas, qtd_valor):
    horas = float(qtd_horas)
    valor = float(qtd_valor)
    if horas <= 40:
        salario = horas * valor
    else:
        extra = horas - 40
        salario = 40 * valor + (extra * (2 * valor))
    return salario


def cal_imc(peso, altura):
    result = peso / altura ** 2
    return round(result, 2)
