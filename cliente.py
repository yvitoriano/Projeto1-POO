
class Aluno:
    def __init__(self, nome, idade, matricula, peso, altura):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.peso = peso
        self.altura = altura

    # Métodos getters e setters
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_peso(self):
        return self.peso
        
    def set_peso(self, peso):
        self.peso = peso

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return round(imc, 2)

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}, Peso: {self.peso}kg, Altura: {self.altura}m")

aluno1 = Aluno("João", 25, "A111", 70, 1.75)
aluno2 = Aluno("Julia", 17, "A222", 62, 1.60)