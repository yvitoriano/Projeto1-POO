from aluno import Aluno
from instrutor import Instrutor
from treino import Treino

# Dados de exemplo
aluno1 = Aluno("Carlos Silva", 22, "A001")
instrutor1 = Instrutor("Mariana Costa", 35, "Musculação")
treino1 = Treino(aluno1, instrutor1, "Treino de força")

def menu():
    print("\nMenu:")
    print("1. Exibir informações do aluno")
    print("2. Exibir informações do instrutor")
    print("3. Exibir informações do treino")
    print("4. Sair")

def exibir_informacoes_aluno():
    print(f"\nInformações do Aluno:")
    print(aluno1)

def exibir_informacoes_instrutor():
    print(f"\nInformações do Instrutor:")
    print(instrutor1)

def exibir_informacoes_treino():
    print(f"\nInformações do Treino:")
    print(treino1)

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_informacoes_aluno()
        elif opcao == '2':
            exibir_informacoes_instrutor()
        elif opcao == '3':
            exibir_informacoes_treino()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
