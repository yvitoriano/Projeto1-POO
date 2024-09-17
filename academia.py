# Classe Academia
class Academia:
    def __init__(self, nome):
        self._nome = nome
        self._instrutores = []
        self._alunos = []

    # Getters
    def get_nome(self):
        return self._nome 

    def get_instrutores(self):
        return self._instrutores

    def get_alunos(self):
        return self._alunos

    # Setters
    def set_nome(self, nome):
        self._nome = nome

    def set_instrutores(self, instrutores):
        self._instrutores = instrutores

    def set_alunos(self, alunos):
        self._alunos = alunos

    def adicionar_instrutor(self, instrutor):
        self._instrutores.append(instrutor)

    def adicionar_aluno(self, aluno):
        self._alunos.append(aluno)  #append : função para adicionar elementos 

    def listar_instrutores(self):
        print(f"Instrutores da academia {self._nome}:")
        for instrutor in self._instrutores:
            print(instrutor)

    def listar_alunos(self):
        print(f"Alunos da academia {self._nome}:")
        for aluno in self._alunos:
            print(aluno)

academia = Academia("FitLife")
print(f"Nome da academia: {academia.get_nome()}")

instrutores.set_instrutores("Julia,Marcos")

print(f"Instrutores da academia: {instrutores.get_instrutores()}")
