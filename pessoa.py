class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if idade > 0:
            self.__idade = idade
        else:
            raise ValueError("Idade deve ser positiva")

    def __str__(self):
        return f"{self.__nome}, {self.__idade} anos"
