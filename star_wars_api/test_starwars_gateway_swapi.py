import unittest
import requests
import mock
from star_wars_api.starwars_api import StarWarsGatewaySWAPI


class StarWarsGatewaySWAPITests(unittest.TestCase):
    def setUp(self):
        self.client = mock.Mock(spec=requests)  # 1
        self.dados_star_wars_gateway = StarWarsGatewaySWAPI(self.client)

    def test_obtem_resposta_do_servidor(self):
        self.client.get.return_value = mock.Mock(status_code=200)  # 2

        resposta = self.dados_star_wars_gateway.buscar_dados()

        self.assertEqual(200, resposta.status_code)
