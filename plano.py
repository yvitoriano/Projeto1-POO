class PlanoDeTreino:
    def __init__(self, nome, duracao, exercicios):
        self._nome = nome
        self._duracao = duracao  # em semanas
        self._exercicios = exercicios

    # Getters
    def get_nome(self):
        return self._nome

    def get_duracao(self):
        return self._duracao

    def get_exercicios(self):
        return self._exercicios

    # Setters
    def set_nome(self, nome):
        self._nome = nome

    def set_duracao(self, duracao):
        self._duracao = duracao

    def set_exercicios(self, exercicios):
        self._exercicios = exercicios

    def __str__(self):
        return f"Plano: {self._nome}, Duração: {self._duracao} semanas, Exercícios: {', '.join(self._exercicios)}"
    
plano1 = PlanoDeTreino("Plano de Resitência", 12, ["Agachamento", "Supino", "Corrida"])
plano2 = PlanoDeTreino("Plano de Hipertrofia", 4, ["Elevação lateral", "Afundo", "flexão"])