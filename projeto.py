# projeto.py

class Projeto:
    def __init__(self, nome, cliente, equipe, status="Em andamento"):
        self.nome = nome
        self.cliente = cliente
        self.equipe = equipe  # Uma lista de objetos Funcionario
        self.status = status
        
    def __str__(self):
        equipe_nomes = ", ".join([func.nome for func in self.equipe])
        return (f"Projeto: {self.nome}\n"
                f"Cliente: {self.cliente.nome}\n"
                f"Equipe: {equipe_nomes}\n"
                f"Status: {self.status}\n")