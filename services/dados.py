import json
import os

PASTA_DB = "database"

def converter_para_dict(obj):
    if isinstance(obj, list):
        return [converter_para_dict(i) for i in obj]
    
    if hasattr(obj, "__dict__"):
        dicionario = {}
        for chave, valor in obj.__dict__.items():
            if chave == "aluno" and hasattr(valor, "_matricula"):
                dicionario[chave] = {"_matricula": valor.matricula}
            elif chave == "turma" and hasattr(valor, "id_turma"):
                dicionario[chave] = {"id_turma": valor.id_turma}
            else:
                dicionario[chave] = converter_para_dict(valor)
        return dicionario
    
    return obj

def salvar_dados(nome_arquivo, dados_objetos):
    if not os.path.exists("database"):
        os.makedirs("database")
        
    caminho = os.path.join("database", f"{nome_arquivo}.json")
    dados_simplificados = converter_para_dict(dados_objetos)
    
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados_simplificados, f, indent=4, ensure_ascii=False)

def carregar_dados(nome_arquivo):
    caminho = os.path.join(PASTA_DB, f"{nome_arquivo}.json")
    if not os.path.exists(caminho):
        return []
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, PermissionError):
        return []
