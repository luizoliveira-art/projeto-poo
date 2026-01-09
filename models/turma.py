class Oferta:
  def __init__(self, nome, duracao, nivel):
    self.nome = str(nome) #nome do curso
    self.duracao = int(duracao)
    self.nivel = str(nivel) #se o curso é nível tecnico, superior, licenciatura ou bacharelado

  def apresentar(self):
    print(f'O curso é {self.nome}')
    print(f'A duração do curso é {self.duracao} meses')
    print(f'O nível do curso é {self.nivel}')
