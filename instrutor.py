from pessoa import Pessoa

class Instrutor(Pessoa):
    def __init__(self, nome, idade, especialidade):
        super().__init__(nome, idade)
        self.__especialidade = especialidade

    def get_especialidade(self):
        return self.__especialidade

    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade

    def __str__(self):
        return f"Instrutor: {super().__str__()}, Especialidade: {self.__especialidade}"
