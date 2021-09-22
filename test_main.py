import main as m


def test_soma_10():
    assert m.soma_10(20) == 30


def test_pagamento():
    assert m.pagamento(50, 10) == 600


def test_cal_imc():
    assert m.cal_imc(80, 1.70) == 27.68
