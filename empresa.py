# empresa.py
from funcionario import Funcionario
from cliente import Cliente
from projeto import Projeto

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.clientes = []
        self.projetos = []
        
    def adicionar_funcionario(self, nome, cargo, especialidade):
        novo_funcionario = Funcionario(nome, cargo, especialidade)
        self.funcionarios.append(novo_funcionario)
        print(f"Funcionário {nome} adicionado.")

    def listar_funcionarios(self):
        print(f"\n--- Funcionários da {self.nome} ---")
        for func in self.funcionarios:
            print(func)
        print("-----------------------------------")
        
    def adicionar_cliente(self, nome, contato):
        novo_cliente = Cliente(nome, contato)
        self.clientes.append(novo_cliente)
        print(f"Cliente {nome} adicionado.")

    def listar_clientes(self):
        print(f"\n--- Clientes da {self.nome} ---")
        for cli in self.clientes:
            print(cli)
        print("----------------------------------")
        
    def criar_projeto(self, nome_projeto, nome_cliente, equipe_nomes):
        # Encontra o cliente
        cliente_obj = next((c for c in self.clientes if c.nome == nome_cliente), None)
        if not cliente_obj:
            print(f"Erro: Cliente '{nome_cliente}' não encontrado.")
            return

        # Encontra os funcionários da equipe
        equipe_obj = [f for f in self.funcionarios if f.nome in equipe_nomes]
        if len(equipe_obj) != len(equipe_nomes):
            print("Erro: Nem todos os funcionários foram encontrados. Verifique os nomes.")
            return

        novo_projeto = Projeto(nome_projeto, cliente_obj, equipe_obj)
        self.projetos.append(novo_projeto)
        print(f"Projeto '{nome_projeto}' criado para o cliente '{nome_cliente}'.")

    def listar_projetos(self):
        print(f"\n--- Projetos da {self.nome} ---")
        for proj in self.projetos:
            print(proj)
        print("-----------------------------------")

    def buscar_projetos_por_funcionario(self, nome_funcionario):
        print(f"\n--- Projetos de {nome_funcionario} ---")
        encontrado = False
        for proj in self.projetos:
            for func in proj.equipe:
                if func.nome == nome_funcionario:
                    print(proj)
                    encontrado = True
                    break
        if not encontrado:
            print(f"Nenhum projeto encontrado para {nome_funcionario}.")
        print("---------------------------------------")