class Aluno(Pessoa):
  def __init__(self, cpf, nome, idade, matricula):
    super().__init__(cpf, nome, idade)
    self.matricula = int(matricula)

  def apresentar(self):
    super().apresentar()
    print(f'Minha matrícula é {self.matricula}\n')
