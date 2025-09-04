# cliente.py

class Cliente:
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato
        
    def __str__(self):
        return f"Nome: {self.nome} | Contato: {self.contato}"