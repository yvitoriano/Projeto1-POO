from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def __str__(self):
        return f"Aluno: {super().__str__()}, Matrícula: {self.__matricula}"
