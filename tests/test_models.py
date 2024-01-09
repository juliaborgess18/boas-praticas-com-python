import sys
sys.path.append(".")

from src.model import pessoa

def test_contatenacao_nome_sobrenome():
    p1 = pessoa.Pessoa('Júlia', 'Borges',22,'F')
    assert p1.nome_completo() == 'Júlia Borges'