import main as m
from bitcoin_transaction import Wallet
from unittest.mock import Mock


def test_soma_10():
    assert m.soma_10(20) == 30


def test_pagamento():
    assert m.pagamento(50, 10) == 600


def test_cal_imc():
    assert m.cal_imc(80, 1.70) == 27.68


def test_carteira_possui_moedas():
    carteira = Wallet(['dfjiw44fds2fw98fgd55'], 1.2)
    assert carteira.destinatarios == ['dfjiw44fds2fw98fgd55']


def test_envio_de_ordem():
    carteira = Wallet(['dfjiw44fds2fw98fgd55'], 1.67)
    assert carteira.enviar_btc(0.34076041) == 'dfjiw44fds2fw98fgd55, saldo = 1.32923959'
