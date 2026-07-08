import banco

banco.criar_tabela()

while True:
    print("\n" + "="*26)
    print(" SISTEMA DE FUNCIONÁRIOS")
    print("="*26)
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionário")
    print("4 - Atualizar funcionário") 
    print("5 - Excluir funcionário") 
    print("0 - Sair")
    print("="*26)

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("\n--- CADASTRAR FUNCIONÁRIO ---")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cargo = input("Cargo: ")
        salario = float(input("Salário: R$"))
        banco.cadastrar_funcionario(nome, idade, cargo, salario)
        
    elif opcao == "2":
        print("\n2--- LISTAR FUNCIONÁRIOS ---")
        banco.listar_funcionarios()

    elif opcao == "3":
        print("\n--- BUSCAR FUNCIONÁRIO ---")
        termo = input("\nDigite o nome ou cargo do funcionário: ")
        banco.buscar_funcionario(termo)

    elif opcao == "4":
        print("\n--- ATUALIZAR FUNCIONÁRIO ---")
        id = int(input("\n Digite o ID do funcionário: "))
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        cargo = input("Novo cargo: ")
        salario = float(input("Novo salário: R$"))
        banco.atualizar_funcionario(id, nome, idade, cargo, salario)

    elif opcao == "5":
        print("\n--- EXCLUIR FUNCIONÁRIO ---")
        banco.listar_funcionarios()
        id = int(input("\nDigite o ID do funcionário a ser excluído: "))
        confirmar = input(f"⚠️  Tem certeza que deseja excluir o funcionário ID {id}? (s/n): ")
        if confirmar.lower() == "s":
            banco.excluir_funcionario(id)
        else:
            print("❌ Exclusão cancelada.")

    elif opcao == "0":
        print("👋 Programa encerrado.")
        break
    else:
        print("\n⚠️  Opção inválida. Tente novamente.")
