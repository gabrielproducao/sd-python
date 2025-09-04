# main.py
from empresa import Empresa

def main():
    # 1. Instanciando a empresa
    nexus_tech = Empresa("Nexus Tech Soluções")
    print(f"Empresa '{nexus_tech.nome}' criada com sucesso!")

    # 2. Adicionando funcionários
    nexus_tech.adicionar_funcionario("Alice", "Gerente de Projetos", "Gestão Ágil")
    nexus_tech.adicionar_funcionario("Bruno", "Desenvolvedor", "Python, Back-end")
    nexus_tech.adicionar_funcionario("Carla", "Designer UI/UX", "Design Digital")
    nexus_tech.adicionar_funcionario("Daniel", "Desenvolvedor", "JavaScript, Front-end")
    nexus_tech.adicionar_funcionario("Eduardo", "Especialista em Redes", "Infraestrutura")

    nexus_tech.listar_funcionarios()
    
    # 3. Adicionando clientes
    nexus_tech.adicionar_cliente("Supermercado Ideal", "joao.ideal@email.com")
    nexus_tech.adicionar_cliente("Academia Corpo Forte", "contato@corpoforte.com")
    
    nexus_tech.listar_clientes()

    # 4. Criando projetos
    # Projeto 1: E-commerce para o supermercado
    nexus_tech.criar_projeto(
        nome_projeto="E-commerce Super Ideal",
        nome_cliente="Supermercado Ideal",
        equipe_nomes=["Alice", "Bruno", "Carla", "Daniel"]
    )
    
    # Projeto 2: Aplicativo móvel para a academia
    nexus_tech.criar_projeto(
        nome_projeto="App Academia Móvel",
        nome_cliente="Academia Corpo Forte",
        equipe_nomes=["Alice", "Bruno", "Daniel"]
    )

    nexus_tech.listar_projetos()

    # 5. Demonstração de funcionalidades extras
    nexus_tech.buscar_projetos_por_funcionario("Alice")
    nexus_tech.buscar_projetos_por_funcionario("Eduardo")
    
if __name__ == "__main__":
    main()