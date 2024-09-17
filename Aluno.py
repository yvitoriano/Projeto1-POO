class aluno:
    def __init__(self, nome, idade, matricula, peso, altura):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.peso = peso
        self.altura = altura

    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self, matricula):
        self.__matricula = matricula
     
    def exibir_info(self):
        print(f"Nome: {self.nome}, Matrícula: {self.__matricula}, Peso: {self.peso}, altura :{self.altura}")
        
    
    


