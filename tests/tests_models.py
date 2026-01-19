import unittest
from models.aluno import Aluno
from models.curso import Curso
from models.turma import Turma
from models.matricula import Matricula

class TestSistemaAcademico(unittest.TestCase):

    def setUp(self):
        self.curso = Curso("ADS", "Analise de Sistemas", 2000)
        self.aluno = Aluno("202601", "Onofre", "onofre@ufca.edu.br")
        self.turma = Turma("T01", self.curso, "2025.2", {}, 2)

    def test_criacao_aluno_valido(self):
        self.assertEqual(self.aluno.nome, "Onofre")
        self.assertEqual(self.aluno.matricula, "202601")

    def test_email_invalido(self):
        with self.assertRaises(ValueError):
            self.aluno.email = "email_errado.com"

    def test_limite_vagas_turma(self):
        aluno2 = Aluno("202602", "Jose", "jose@ufca.edu.br")
        mat1 = Matricula(self.aluno, self.turma)
        mat2 = Matricula(aluno2, self.turma)
        
        self.turma.matriculas.append(mat1)
        self.turma.matriculas.append(mat2)
        
        self.assertEqual(len(self.turma.matriculas), 2)

    def test_calculo_cr(self):
        mat = Matricula(self.aluno, self.turma)
        mat.nota = 10.0
        mat.situacao = 'APROVADO'
        self.aluno.historico.append(mat)
        
        self.assertEqual(self.aluno.cr, 10.0)

    def test_nota_fora_do_limite(self):
        mat = Matricula(self.aluno, self.turma)
        with self.assertRaises(ValueError):
            mat.nota = 11.0

if __name__ == "__main__":
    unittest.main()
