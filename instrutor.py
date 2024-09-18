from cliente import Aluno
from plano import PlanoDeTreino
from academia import Academia
class Instrutor:
    def __init__(self, nome, matricula, especialidade):
        self.nome = nome
        self.matricula = matricula
        self.especialidade = especialidade

    def get_nome(self):
        return self.nome
       
    def set_nome(self, nome):
        self.nome = nome

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_especialidade(self):
        return self.especialidade

    def set_especialidade(self, especialidade):
        self.especialidade = especialidade

    def criar_treino(self, aluno, plano_de_treino):
        print(f"O instrutor {self.nome} criou um treino {plano_de_treino.get_nome()} para o aluno {aluno.get_nome()}. Dados do treino :(plano_de_treino)")

instrutor1 = Instrutor("Mariane","I111","Musculação")
instrutor2 = Instrutor("Ícaro","I222","Musculação")