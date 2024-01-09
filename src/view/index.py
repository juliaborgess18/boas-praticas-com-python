import sys
from pathlib import Path 
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controller.pessoa import PessoaController
from model.pessoa import Pessoa 

while True:

    decisao = int(input('Digite 1 para salvar e 2 para listar: '))

    if decisao == 1:
        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        idade = input('Idade: ')
        sexo = input('Sexo: ')

        p1 = Pessoa(nome=nome, sobrenome=sobrenome, idade=idade, sexo=sexo)
        PessoaController.salvar_pessoa(p1)
        
    elif decisao == 2:
        for p in PessoaController.listar_pessoas():
            print(f'Nome: {p.nome} {p.sobrenome}')