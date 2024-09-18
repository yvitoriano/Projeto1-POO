from cliente import Aluno
from instrutor import Instrutor
from plano import PlanoDeTreino
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
        self._alunos.append(aluno)

    def listar_instrutores(self):
        print(f"Instrutores da academia {self._nome}:")
        for instrutor in self._instrutores:
            print(instrutor.get_nome())

    def listar_alunos(self):
        print(f"Alunos da academia {self._nome}:")
        for aluno in self._alunos:
            print(aluno.get_nome())

    # Menu
    def menu_acesso(self):
        while True:
            print("\n--- Menu da Academia ---")
            print("1. Acesso do Aluno")
            print("2. Acesso do Instrutor")
            print("3. Acesso do Dono (Admin)")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.menu_aluno()
            elif opcao == '2':
                self.menu_instrutor()
            elif opcao == '3':
                self.menu_admin()
            elif opcao == '4':
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    # Menu Aluno
    def menu_aluno(self):
        print("\n--- Menu do Aluno ---")
        aluno_matricula = input("Informe a matrícula do aluno: ")
        aluno = self.buscar_aluno_por_matricula(aluno_matricula)
        if aluno:
            aluno.exibir_informacoes()
            print(f"IMC: {aluno.calcular_imc()}")
        else:
            print("Aluno não encontrado.")

    # Menu Instrutor
    def menu_instrutor(self):
        print("\n--- Menu do Instrutor ---")
        instrutor_matricula = input("Informe a matrícula do instrutor: ")
        instrutor = self.buscar_instrutor_por_matricula(instrutor_matricula)
        if instrutor:
            instrutor.criar_treino()
        else:
            print("Instrutor não encontrado.")

    # Menu Dono/Admin
    def menu_admin(self):
        print("\n--- Menu do Dono (Admin) ---")
        print("1. Listar Alunos")
        print("2. Listar Instrutores")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            self.listar_alunos()
        elif escolha == '2':
            self.listar_instrutores()
        else:
            print("Opção inválida.")

    # Funções auxiliares
    def buscar_aluno_por_matricula(self, matricula):
        for aluno in self._alunos:
            if aluno.get_matricula() == matricula:
                return aluno
        return None

    def buscar_instrutor_por_matricula(self, matricula):
        for instrutor in self._instrutores:
            if instrutor.get_matricula() == matricula:
                return instrutor
        return None
    
