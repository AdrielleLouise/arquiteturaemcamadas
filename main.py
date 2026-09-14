from negocio import *
while True:
  print("========== Controle de Manutenção Doméstica ==========")
  print("1 - Cadastrar Manutenção")
  print("2 - Consultar Manutenção")
  print("3 - Realizar Manutenção")
  print("4 - Listar Manutenções")
  print("5 - Remover cadastro existente")
  print("6 - Sair")
  opcao = input("Escolha uma opção: ")
  if opcao == "1":
    nome = input("Nome do equipamento: ")
    tipo = input("Manutenção a ser realizada: ")
    periodicidade = int(input("periodicidade (em dias): "))
    ultima_manutencao = input("Data da última manutenção (em dd/mm/aaaa): ")
    sucesso, mensagem = cadastrar_manutencao(
        nome,
        tipo,
        periodicidade,
        ultima_manutencao
    )
    print(mensagem)
  elif opcao == "2":
    nome = input("Nome do equipamento: ")
    sucesso, resultados = consultar_manutencao(nome)
    if sucesso:
      print("\n==========", nome, "==========")
      for resultado in resultados:
        print("\nEquipamento:", resultado["nome"])
        print("Manutenção:", resultado["tipo"])
        print("Última manutenção:", resultado["ultima_manutencao"])
        print("Previsão de Manutenção:", resultado["proxima_manutencao"])
        print("Status da manutenção:", resultado["status"])
    else:
      print(resultados)
  elif opcao == "3":
    nome = input("Nome do equipamento: ")
    tipo = input("Manutenção realizada: ")
    data_realizada = input("Data da realização (dd/mm/aaaa): ")
    sucesso, mensagem = realizar_manutencao(nome, tipo, data_realizada)
    print(mensagem)
  elif opcao == "4":
    sucesso, resultados = listar_manutencoes()
    if sucesso:
      print("\n============ Manutenções Cadastradas ============")
      for resultado in resultados:
        print("\nEquipamento:", resultado["nome"])
        print("Manutenção:", resultado["tipo"])
        print("Última manutenção:", resultado["ultima_manutencao"])
        print("Previsão de Manutenção:", resultado["proxima_manutencao"])
        print("Status da manutenção:", resultado["status"])
    else:
      print(resultados)
  elif opcao == "5":
    while True:
      print("\n ========= Remover Cadastro Existente ==========")
      print("1 - Remover equipamento específico")
      print("2 - Remover manutenção específica")
      print("3 - Voltar")
      opcao_remover = input("Escolha uma opção: ")
      if opcao_remover == "1":
        nome = input("Nome do equipamento: ")
        sucesso, mensagem = remover_equipamento_cadastrado(nome)
        print(mensagem)
      elif opcao_remover == "2":
        nome = input("Nome do equipamento: ")
        tipo = input("Manutenção a ser removida: ")
        sucesso, mensagem = remover_manutencao_cadastrada(nome, tipo)
        print(mensagem)
      elif opcao_remover == "3":
        break
      else:
        print("Opção inválida!")
  elif opcao == "6":
    print("Controle encerrado. Até mais! :)")
    break
  else:
    print("Opção inválida!")