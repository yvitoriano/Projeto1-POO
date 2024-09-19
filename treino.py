class Treino:
    def __init__(self, aluno, instrutor, descricao):
        self.__aluno = aluno
        self.__instrutor = instrutor
        self.__descricao = descricao

    def get_aluno(self):
        return self.__aluno

    def set_aluno(self, aluno):
        self.__aluno = aluno

    def get_instrutor(self):
        return self.__instrutor

    def set_instrutor(self, instrutor):
        self.__instrutor = instrutor

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def __str__(self):
        return (f"Treino: {self.__descricao}\n"
                f"Aluno: {self.__aluno}\n"
                f"Instrutor: {self.__instrutor}")
