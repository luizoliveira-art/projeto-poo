from models.oferta import Oferta

class Turma(Oferta):
    def __init__(self, id_turma, curso_obj, semestre, horarios, vagas):
        super().__init__(curso_obj.nome, 6) 
        self.id_turma = id_turma
        self.curso = curso_obj
        self.semestre = semestre
        self.horarios = horarios
        self.vagas = vagas
        self.matriculas = []

    @property
    def vagas(self):
        return self._vagas

    @vagas.setter
    def vagas(self, valor):
        if valor < 0: 
            raise ValueError("Vagas não podem ser negativas.")
        self._vagas = valor

    def __len__(self):
        return len(self.matriculas)

    def __str__(self):
        return f"Turma {self.id_turma} - {self.nome_curso} ({self.semestre})"
