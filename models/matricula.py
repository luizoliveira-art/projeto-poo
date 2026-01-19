class Matricula:
    def __init__(self, aluno, turma):
        self.aluno = aluno
        self.turma = turma
        self._nota = 0.0
        self._frequencia = 0.0
        self.situacao = "CURSANDO"

    @property
    def nota(self): return self._nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10: 
            self._nota = float(valor)
        else: 
            raise ValueError("Nota deve ser entre 0 e 10.")

    @property
    def frequencia(self): return self._frequencia

    @frequencia.setter
    def frequencia(self, valor):
        if 0 <= valor <= 100: 
            self._frequencia = float(valor)
        else: 
            raise ValueError("Frequência deve ser entre 0 e 100.")

    def processar_situacao(self, nota_min=6.0, freq_min=75.0):
        if self.frequencia < freq_min: 
            self.situacao = "REPROVADO_POR_FREQUENCIA"
        elif self.nota < nota_min: 
            self.situacao = "REPROVADO_POR_NOTA"
        else: 
            self.situacao = "APROVADO"

    def __str__(self):
        return f"{self.turma.id_turma}: Nota {self.nota} | Freq {self.frequencia}% | {self.situacao}"
