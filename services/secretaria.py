from datetime import datetime

class Secretaria:
    @staticmethod
    def checar_choque(horarios_turma_nova, matriculas_existentes):
        for mat in matriculas_existentes:
            turma_ativa = mat.turma
            for dia, intervalo in horarios_turma_nova.items():
                if dia in turma_ativa.horarios:
                    h1_inicio, h1_fim = [datetime.strptime(t, "%H:%M") for t in intervalo.split("-")]
                    h2_inicio, h2_fim = [datetime.strptime(t, "%H:%M") for t in turma_ativa.horarios[dia].split("-")]
                    
                    if max(h1_inicio, h2_inicio) < min(h1_fim, h2_fim):
                        return True
        return False

    @staticmethod
    def matricular(aluno, turma):
        if len(turma) >= turma.vagas:
            raise ValueError("Falha: Turma lotada.")

        codigos_aprovados = [m.turma.curso.codigo for m in aluno.historico if m.situacao == "APROVADO"]
        for pre in turma.curso.pre_requisitos:
            if pre not in codigos_aprovados:
                raise ValueError(f"Falha: Pré-requisito {pre} não cumprido.")

        matriculas_periodo = [m for m in aluno.historico if m.turma.semestre == turma.semestre]
        if Secretaria.checar_choque(turma.horarios, matriculas_periodo):
            raise ValueError("Falha: Choque de horário detectado.")

        from models.matricula import Matricula
        nova_matricula = Matricula(aluno, turma)
        turma.matriculas.append(nova_matricula)
        aluno.historico.append(nova_matricula)
        return nova_matricula
