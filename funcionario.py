# funcionario.py

class Funcionario:
    def __init__(self, nome, cargo, especialidade):
        self.nome = nome
        self.cargo = cargo
        self.especialidade = especialidade
        
    def __str__(self):
        return f"Nome: {self.nome} | Cargo: {self.cargo} | Especialidade: {self.especialidade}"