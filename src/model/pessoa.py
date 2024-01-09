class Pessoa:
    
    def __init__(self, nome, sobrenome, idade, sexo):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.idade = idade 
        self.sexo = sexo 
    
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'