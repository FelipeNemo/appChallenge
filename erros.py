"""Modulo que implementa as classes erros da app.py"""

#Class Usuario
class ErroDeRequisicao(Exception):
    """Erro de requisição"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroDeRequisicao (" + self.__msg +")"
    
class ErroDeConsulta(Exception):
    """Erro de requisição"""
    def __init__(self, mensagem):
        self.__msg=mensagem
    def __str__(self):
        return "ErroDeConsulta (" + self.__msg +")"
