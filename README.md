# Sistema de Gerenciamento Acadêmico - UFCA

Projeto desenvolvido para a disciplina de Programação Orientada a Objetos (POO) do curso de ADS (UFCA). O sistema realiza o gerenciamento completo de cursos, alunos, turmas e matrículas com persistência em arquivos JSON.

## 🚀 Funcionalidades (CRUD Completo)
- **Gestão de Cadastros:** Cadastro, edição e exclusão de Alunos e Cursos.
- **Operações Acadêmicas:** Abertura de turmas, matrículas e lançamento de notas/frequência.
- **Relatórios:** Ranking de alunos por CR (Coeficiente de Rendimento) e status de ocupação de turmas.
- **Persistência de Dados:** Reconstrução automática de objetos e seus relacionamentos ao iniciar o sistema.
- **Interface CLI:** Menus organizados em subcategorias, limpeza de tela e validações de entrada.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.13.1 (ou superior)
- **Módulos Nativos:** `os`, `json`, `unittest`

## 📂 Estrutura do Projeto
- `models/`: Classes base com aplicação de Herança e Encapsulamento.
- `services/`: Lógica de persistência e conversão de objetos para JSON.
- `database/`: Pasta destinada ao armazenamento dos arquivos de dados.
- `tests/`: Suíte de testes unitários para validação das regras de negócio.

## ⚙️ Como Executar o Programa
1. Certifique-se de que possui o Python instalado em sua máquina.
2. Abra o terminal na pasta raiz do projeto.
3. Execute o comando:
   ```bash
   python3 main.py
