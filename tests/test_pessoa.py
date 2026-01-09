import pytest
from models.pessoa import Pessoa

def test_criacao_pessoa_valida():
    p = Pessoa('Maria', 'maria@email.com')
    assert p.nome == 'Maria'
    assert p.email == 'maria@email.com'
    
def test_nome_vazio():
    p = Pessoa('Pedro', 'pedro@email.com')
    with pytest.raises(ValueError, match='O nome não pode estar vazio'):
        p.nome = ''
    
def test_email_invalido():
    p = Pessoa('João', 'joao@email.com')
    with pytest.raises(ValueError, match='E-mail inválido'):
        p.email = 'teste-email.com'
