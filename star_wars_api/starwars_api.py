# coding=utf-8
import requests


class StarWarsGatewaySWAPI(object):
    URL = 'http://swapi.co/api/'

    def __init__(self, client_http):
        self.client = client_http

    def buscar_dados(self):
        return self.client.get(self.URL)
