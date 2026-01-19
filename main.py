import os
from models.aluno import Aluno
from models.curso import Curso
from models.turma import Turma
from models.matricula import Matricula
from services.dados import salvar_dados, carregar_dados

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    print("\n" + "="*40)
    print("      SISTEMA ACADÊMICO UFCA")
    print("="*40)
    print("1. Gestão de Cadastros (Cursos/Alunos)")
    print("2. Operações Acadêmicas (Turmas/Notas)")
    print("3. Relatórios e Estatísticas")
    print("4. Salvar e Sair")
    print("="*40)
    return input("Escolha uma categoria: ")

def main():
    cursos = [Curso(c['_codigo'], c['_nome'], c['_carga_horaria']) for c in carregar_dados("cursos")]
    alunos = [Aluno(a['_matricula'], a['_nome'], a['_email']) for a in carregar_dados("alunos")]
    
    turmas_data = carregar_dados("turmas")
    turmas = []
    for t in turmas_data:
        cod_curso = t.get('curso', {}).get('_codigo')
        curso_obj = next((c for c in cursos if c.codigo == cod_curso), None)
        
        if curso_obj:
            nova_t = Turma(t.get('id_turma'), curso_obj, t.get('semestre'), t.get('horarios', {}), t.get('_vagas', 0))
            
            for m_dict in t.get('matriculas', []):
                mat_aluno = m_dict.get('aluno', {}).get('_matricula')
                aluno_obj = next((a for a in alunos if a.matricula == mat_aluno), None)
                
                if aluno_obj:
                    nova_m = Matricula(aluno_obj, nova_t)
                    nova_m.nota = m_dict.get('_nota', 0.0)
                    nova_m.frequencia = m_dict.get('_frequencia', 0.0)
                    nova_m.situacao = m_dict.get('situacao', 'CURSANDO')
                    nova_t.matriculas.append(nova_m)
                    aluno_obj.historico.append(nova_m)
                    
            turmas.append(nova_t)

    while True:
        limpar_tela()
        opcao = menu_principal()

        if opcao == "1":
            limpar_tela()
            print("\n--- GESTÃO DE CADASTROS ---")
            print("1. Gerenciar Cursos")
            print("2. Gerenciar Alunos")
            print("3. Voltar")
            sub = input("Opção: ")
            
            if sub == "1":
                limpar_tela()
                print("\n[A] Novo Curso | [E] Editar | [D] Deletar")
                cmd = input("Ação: ").upper().strip()[0]
                
                if cmd == 'A':
                    cod = input("Código: ").upper().strip()
                    if not any(c.codigo == cod for c in cursos):
                        nome = input("Nome: ")
                        ch = int(input("Carga Horária: "))
                        cursos.append(Curso(cod, nome, ch))
                        print("- Sucesso: Curso adicionado.")
                    else: 
                        print("- Erro: Código já existe.")
                        
                elif cmd == 'E' and cursos:
                    for i, c in enumerate(cursos): 
                        print(f"[{i}] {c.nome}")
                        
                    idx = int(input("Índice: "))
                    cursos[idx].carga_horaria = int(input("Nova CH: "))
                    print("- Curso atualizado.")
                elif cmd == 'D' and cursos:
                    for i, c in enumerate(cursos): 
                        print(f"[{i}] {c.nome}")
                        
                    cursos.pop(int(input("Índice: ")))
                    print("- Curso removido.")
                input("\nPressione Enter para continuar...")

            elif sub == "2":
                limpar_tela()
                print("\n[A] Novo Aluno | [E] Editar | [D] Deletar")
                cmd = input("Ação: ").upper().strip()[0]
                
                if cmd == 'A':
                    mat = input("Matrícula: ")
                    if not any(a.matricula == mat for a in alunos):
                        nome = input("Nome: ")
                        email = input("E-mail: ")
                        alunos.append(Aluno(mat, nome, email))
                        print("- Sucesso: Aluno adicionado.")
                    else: 
                        print("- Erro: Matrícula já existe.")
                elif cmd == 'E' and alunos:
                    for i, a in enumerate(alunos): 
                        print(f"[{i}] {a.nome}")
                        
                    idx = int(input("Índice: "))
                    alunos[idx].email = input("Novo E-mail: ")
                    print("- Dados atualizados.")
                elif cmd == 'D' and alunos:
                    for i, a in enumerate(alunos): 
                        print(f"[{i}] {a.nome}")
                        
                    alunos.pop(int(input("Índice: ")))
                    print("- Aluno removido.")
                input("\nPressione Enter para continuar...")

        elif opcao == "2":
            limpar_tela()
            print("\n--- OPERAÇÕES ACADÊMICAS ---")
            print("1. Abrir Nova Turma")
            print("2. Matricular Aluno")
            print("3. Lançar Notas/Frequência")
            print("4. Voltar")
            sub = input("Opção: ")
            
            if sub == "1" and cursos:
                for i, c in enumerate(cursos): 
                    print(f"[{i}] {c}")
                    
                idx = int(input("Curso: "))
                id_t = input("ID Turma: ").upper()
                sem = input("Semestre: ")
                vagas = int(input("Vagas: "))
                turmas.append(Turma(id_t, cursos[idx], sem, {}, vagas))
                print("- Turma aberta com sucesso.")
            elif sub == "2" and alunos and turmas:
                for i, a in enumerate(alunos): 
                    print(f"[{i}] {a.nome}")
                    
                aluno = alunos[int(input("Aluno: "))]
                for i, t in enumerate(turmas): 
                    print(f"[{i}] {t.id_turma}")
                    
                turma = turmas[int(input("Turma: "))]
                if len(turma.matriculas) < turma.vagas:
                    m = Matricula(aluno, turma)
                    turma.matriculas.append(m)
                    aluno.historico.append(m)
                    print("- Matrícula confirmada.")
            elif sub == "3" and turmas:
                for i, t in enumerate(turmas): 
                    print(f"[{i}] {t.id_turma}")
                    
                t_sel = turmas[int(input("Turma: "))]
                for i, m in enumerate(t_sel.matriculas): 
                    print(f"[{i}] {m.aluno.nome}")
                    
                m_sel = t_sel.matriculas[int(input("Aluno: "))]
                m_sel.nota = float(input("Nota: "))
                m_sel.frequencia = float(input("Frequência: "))
                m_sel.processar_situacao()
                print("- Notas lançadas.")
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            limpar_tela()
            print("\n--- RELATÓRIOS ---")
            print("1. Ranking de Alunos (CR)")
            print("2. Ocupação de Turmas")
            print("3. Voltar")
            sub = input("Opção: ")
            
            if sub == "1":
                print("\nRanking por Coeficiente de Rendimento:")
                for a in sorted(alunos, reverse=True): 
                    print(f"- {a.nome.ljust(15)} | CR: {a.cr}")
                    
            elif sub == "2":
                print("\nStatus de Ocupação das Turmas:")
                for t in turmas: 
                    print(f"- Turma {t.id_turma}: {len(t.matriculas)}/{t.vagas} vagas")
                    
            input("\nPressione Enter para voltar ao menu principal...")

        elif opcao == "4":
            print("- Salvando dados em database/...")
            salvar_dados("cursos", cursos)
            salvar_dados("alunos", alunos)
            salvar_dados("turmas", turmas)
            print("- Sistema encerrado com segurança.")
            break

if __name__ == "__main__":
    main()
