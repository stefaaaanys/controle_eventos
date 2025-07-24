eventos = []
codigo_evento = 1  # fora da função para não reiniciar a cada novo usuário

def definindo_usuario():
    global codigo_evento
    nome_usuario = input("\nDigite o seu primeiro e último nome: ").strip()
    encontrado = False

    with open("usuario", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            nome, tipo = linha.replace('"', '').split(",")
            nome = nome.strip()
            tipo = tipo.strip()

            if nome_usuario == nome:
                encontrado = True
                print("Usuário encontrado!")

                # --- RESPONSÁVEL ---
                if tipo == "responsavel":
                    while True:
                        print("\nMenu para os responsáveis dos eventos:")
                        print("0 - Sair")
                        print("2 - Cadastrar evento")
                        print("3 - Visualizar eventos")
                        print("4 - Atualizar evento\n")

                        opcao = int(input("Escolha uma opção: "))

                        if opcao == 0:
                            print("Encerrando sessão do usuário responsável...\n")
                            break

                        elif opcao == 2:
                            nome_evento = input("Digite o nome do evento: ")
                            data = input("Digite a data do evento: ")
                            vagas = int(input("Digite a quantidade de vagas disponíveis para esse evento: "))
                            descricao = input("Digite uma breve descrição do evento: ")

                            evento = {
                                "codigo": codigo_evento,
                                "nome": nome_evento,
                                "data": data,
                                "vagas": vagas,
                                "descrição": descricao,
                                "inscrições": 0,
                                "inscritos": []
                            }

                            eventos.append(evento)
                            print(f"Evento {nome_evento} adicionado com o código {codigo_evento}")
                            codigo_evento += 1

                        elif opcao == 3:
                            print("\nEventos disponíveis:")
                            for e in eventos:
                                print(f"\nNome: {e['nome']}\nData: {e['data']}\nVagas: {e['vagas']}\nInscritos: {e['inscrições']}\nDescrição: {e['descrição']}")

                        elif opcao == 4:
                            procurar_evento = input("Digite o nome do evento: ")
                            evento_encontrado = None

                            for e in eventos:
                                if e["nome"].lower() == procurar_evento.lower():
                                    evento_encontrado = e
                                    break

                            if evento_encontrado:
                                print("\n1- Modificar nome do evento")
                                print("2- Modificar data do evento")
                                print("3- Modificar a quantidade de vagas")
                                print("4- Modificar a descrição")
                                print("5- Excluir evento")
                                print("6- Voltar à página inicial")

                                atualizacao = int(input("O que deseja atualizar? "))

                                if atualizacao == 1:
                                    novo_nome = input("Digite o novo nome do evento: ")
                                    evento_encontrado["nome"] = novo_nome
                                    print("Nome atualizado com sucesso!")
                                elif atualizacao == 2:
                                    nova_data = input("Digite a nova data do evento: ")
                                    evento_encontrado["data"] = nova_data
                                    print("Data atualizada com sucesso!")
                                elif atualizacao == 3:
                                    qtd_v = int(input("Digite a nova quantidade de vagas: "))
                                    evento_encontrado["vagas"] = qtd_v
                                    print("Quantidade de vagas atualizada com sucesso!")
                                elif atualizacao == 4:
                                    nova_desc = input("Digite a nova descrição do evento: ")
                                    evento_encontrado["descrição"] = nova_desc
                                    print("Descrição atualizada com sucesso!")
                                elif atualizacao == 5:
                                    eventos.remove(evento_encontrado)
                                    print("Evento excluido")
                                elif atualizacao == 6:
                                    print("Voltando ao menu...")
                                else:
                                    print("Opção inválida")
                            else:
                                print("Evento não encontrado.")

                # --- ALUNO ---
                elif tipo == "aluno":
                    while True:
                        print("\nMenu para alunos:")
                        print("0 - Sair")
                        print("1 - Visualizar eventos")
                        print("2 - Se inscrever em um evento\n")
                        opcao = int(input("Escolha uma opção: "))

                        if opcao == 0:
                            print("Encerrando sessão do aluno...\n")
                            break

                        elif opcao == 1:
                            print("\nEventos disponíveis:")
                            for e in eventos:
                                vagas_disponiveis = e["vagas"] - e["inscrições"]
                                print(f"\nNome: {e['nome']}\nData: {e['data']}\nDescrição: {e['descrição']}\nVagas disponíveis: {vagas_disponiveis}")

                        elif opcao == 2:
                            nome_evento = input("Digite o nome do evento que deseja se inscrever: ")
                            evento_encontrado = None

                            for e in eventos:
                                if e["nome"].lower() == nome_evento.lower():
                                    evento_encontrado = e
                                    break

                            if evento_encontrado:
                                vagas_restantes = evento_encontrado["vagas"] - evento_encontrado["inscrições"]
                                if vagas_restantes > 0:
                                    if nome_usuario in evento_encontrado["inscritos"]:
                                        print("Você já está inscrito neste evento.")
                                    else:
                                        evento_encontrado["inscrições"] += 1
                                        evento_encontrado["inscritos"].append(nome_usuario)
                                        print(f"Inscrição realizada com sucesso no evento: {evento_encontrado['nome']}")
                                else:
                                    print("Não há vagas disponíveis para este evento.")
                            else:
                                print("Evento não encontrado.")

                else:
                    print("Tipo de usuário não reconhecido.")
                break

    if not encontrado:
        print("Usuário não encontrado...")

# Loop principal
while True:
    definindo_usuario()