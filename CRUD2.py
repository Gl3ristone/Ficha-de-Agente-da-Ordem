import json
import random
def menu():
    print('''Bem-vindo à FAO
Ficha dos Agentes da Ordem
Opções:
1. Criar
2. Listar
3. Buscar
4. Editar
5. Excluir
6. Rolar Dados
7. Batalha
0. Sair
''')
def salvar(ordem, filename = "dados.json"):
    with open(filename, 'w') as f:
        json.dump(ordem, f)
def criar(ordem):
    id_agente = input('ID do agente: ')
    nome = input('Nome do Agente: ')
    forca = int(input('Força do Agente: '))
    agilidade = int(input('Agilidade do Agente: '))
    intelecto = int(input('Intelecto do Agente: '))
    presenca = int(input('Presença do Agente: '))
    vigor = int(input('Vigor do Agente: '))
    origem = input('Origem: ')
    classe = input('Classe (Combatente, Especialista, Ocultista): ').capitalize()
    trilha = input('Trilha da Classe: ')
    nex = int(input('Nível de Exposição: '))

    if classe == 'Combatente':
        pv = 20 + vigor + (4*((nex-5)//5)+vigor)
        pe = 2 + presenca + (2*((nex-5)//5)+presenca)
        sanidade = 12 + (3*((nex-5)//5))
    elif classe == 'Especialista':
        pv = 16 + vigor + (3*((nex-5)//5)+vigor)
        pe = 3 + presenca + (3*((nex-5)//5)+presenca)
        sanidade = 16 + (4*((nex-5)//5))
    elif classe == 'Ocultista':
        pv = 12 + vigor + (2*((nex-5)//5)+vigor)
        pe = 4 + presenca + (4*((nex-5)//5)+presenca)
        sanidade = 20 + (5*((nex-5)//5))
    else:
        print("Classe inválida! Usando valores padrão.")
        pv = 10 + vigor
        pe = 2 + presenca
        sanidade = 10

    agente = {
        'id': id_agente,
        'nome': nome,
        'atributos': {
            'forca': forca,
            'agilidade': agilidade,
            'intelecto': intelecto,
            'presenca': presenca,
            'vigor': vigor
        },
        'origem': origem,
        'classe': classe,
        'trilha': trilha,
        'nex': nex,
        'pv': pv,
        'pe': pe,
        'sanidade': sanidade
    }

    ordem.append(agente)

def listar(ordem):
    if not ordem:
        print('Nenhum agente cadastrado.')
    else:
        for agente in ordem:
            print(f"ID: {agente['id']}, Nome: {agente['nome']}, Origem: {agente['origem']}, "
                  f"Classe: {agente['classe']}, Trilha: {agente['trilha']}, Nex: {agente['nex']}%")

def buscar(ordem):
    buscavel = input('ID do agente desejado: ')
    for agente in ordem:
        if agente['id'] == buscavel:
            print(f"ID: {agente['id']} | Nome: {agente['nome']} | Origem: {agente['origem']}")
            print(f"Classe: {agente['classe']} | Trilha: {agente['trilha']} | Nex: {agente['nex']}%")
            print(f"Atributos: {agente['atributos']}")
            print(f"PV: {agente['pv']} | PE: {agente['pe']} | Sanidade: {agente['sanidade']}")
            return
    print(f'Nenhum agente com ID: {buscavel} encontrado')
def editar(ordem):
    buscavel = input('ID do agente desejado: ')
    for agente in ordem:
        if agente['id'] == buscavel:
            print(f"ID: {agente['id']}, Nome: {agente['nome']}, Origem: {agente['origem']}, "
                  f"Classe: {agente['classe']}, Trilha: {agente['trilha']}, Nex: {agente['nex']}%")

            novos_dados = {
                'nome': input('Novo nome do agente: '),
                'origem': input('Nova origem: '),
                'classe': input('Nova classe: ').capitalize(),
                'trilha': input('Nova trilha da classe: '),
                'nex': int(input('Novo nível de exposição: '))
            }
            agente.update(novos_dados)

            print("Digite os novos atributos:")
            novos_atributos = {}
            for atr in agente['atributos']:
                novos_atributos[atr] = int(input(f"{atr.capitalize()}: "))
            agente['atributos'].update(novos_atributos)

            vigor = agente['atributos']['vigor']
            presenca = agente['atributos']['presenca']
            nex = agente['nex']

            classe = agente['classe']
            if classe == 'Combatente':
                agente['pv'] = 20 + vigor + (4*((nex-5)//5) + vigor)
                agente['pe'] = 2 + presenca + (2*((nex-5)//5) + presenca)
                agente['sanidade'] = 12 + (3*((nex-5)//5))
            elif classe == 'Especialista':
                agente['pv'] = 16 + vigor + (3*((nex-5)//5) + vigor)
                agente['pe'] = 3 + presenca + (3*((nex-5)//5) + presenca)
                agente['sanidade'] = 16 + (4*((nex-5)//5))
            elif classe == 'Ocultista':
                agente['pv'] = 12 + vigor + (2*((nex-5)//5) + vigor)
                agente['pe'] = 4 + presenca + (4*((nex-5)//5) + presenca)
                agente['sanidade'] = 20 + (5*((nex-5)//5))
            else:
                print("Classe inválida! Valores não atualizados.")

            print("Ficha atualizada com sucesso.")
            return
    print(f'Nenhum agente com ID: {buscavel} encontrado')
def excluir(ordem):
    buscavel = input('ID do agente desejado: ')
    for agente in ordem:
        if agente['id'] == buscavel:
            print(f"ID: {agente['id']}, Nome: {agente['nome']}, Origem: {agente['origem']}, "
                  f"Classe: {agente['classe']}, Trilha: {agente['trilha']}, Nex: {agente['nex']}%")
            resposta = int(input('Digite 1 para confirmar a exclusão da ficha'))
            if resposta == 1:
                ordem.remove(agente)
                print('FICHA EXCLUÍDA')
            else:
                print('ficha na excluida')
                
            return
    print(f'Nenhum agente com ID: {buscavel} encontrado')
def teste(ordem, criaturas):
    opcao = int(input('Que tipo de roll voce quer?\n1. Pericia \n2. Ataque\n3. Livre'))
    if opcao == 1:
        buscado = input('Id do Agente: ')
        for agente in ordem:
            if agente['id'] == buscado:
                atr = input('Escolha um Atributo: Força, Agilidade, Vigor, Intelecto, Presenca').lower()
                if atr in agente['atributos']:
                    quant = agente['atributos'][atr]
                    bonus = int(input('Bonus de pericia e etc'))
                    roll = [random.randint(1,20) for _ in range(quant)]
                    print(f'Rolagem: {sorted(roll)}')
                    print(f'Resultado: {max(roll)+bonus}')
    elif opcao == 2:
        buscado = input('ID do Agente: ')
        for agente in ordem:
            if agente['id'] == buscado:
                print(criaturas)
                id_inimigo = input('ID do INIMIGO: ')
                for inimigo in criaturas:
                    if inimigo['id'] == id_inimigo:
                        atr = input('Escolha um Atributo: Força, Agilidade, Vigor, Intelecto, Presenca').lower()
                        if atr in agente['atributos']:
                            quant = agente['atributos'][atr]
                            bonus = int(input('Bonus de pericia e etc'))
                            roll = [random.randint(1,20) for _ in range(quant)]
                            resultado = max(roll)+bonus
                            print(f'Rolagem: {sorted(roll)}')
                            print(f'Resultado: {resultado}')
                            if resultado >= inimigo['defesa']:
                                print(f"{agente['nome']} acerta {inimigo['nome']}")
                                qdano = int(input('Quantidade de dados de Dano: '))
                                ldano = int(input('Lados maximos do dado: '))
                                bdano = int(input('Bonus no dano'))
                                if (resultado-bonus) == 20:
                                    roll_dano = [random.randint(1,ldano) for _ in range(qdano*2)]
                                else:
                                    roll_dano = [random.randint(1,ldano) for _ in range(qdano)]
                                
                                
                                print(f'Roll de dano:{roll_dano} \nResultado Final: {sum(roll_dano)+bdano}')
                                inimigo['vida'] -= sum(roll_dano)+bdano
                                if inimigo['vida'] < 1:
                                    print(f"{inimigo['nome']} foi derrotado")
                                    criaturas.remove(inimigo)
                                else: print(f"{inimigo['nome']} está com {inimigo['vida']} de PV sobrando")
    elif opcao == 3: 
        quant = int(input('Quantidade de dados'))
        lado = int(input('Maximo de lados em cada dado'))
        resultado = [random.randint(1,lado) for _ in range(quant)]
        print(f'Rolagens: {resultado}')
        print(f'Soma: {sum(resultado)}')

def batalha(criaturas):
    opcao = int(input('Deseja adcionar uma criatura? \n1- S\n0- N'))
    while opcao != 0:
        idc = input('ID do Inimigo: ')
        nome = input('Nome do inimigo: ')
        vida = int(input('Vida do Inimigo: '))
        dfs =  int(input('Defesa do Inimigo: '))
        inimigo = {'id': idc,
            'nome': nome,
            'vida': vida,
            'defesa': dfs
        } 
        criaturas.append(inimigo)
        opcao = int(input('Deseja adcionar uma criatura? \n1- S\n0- N'))

def inicio():
    resposta = 1
    criaturas = []
    try:
        with open('dados.json', 'r', encoding='utf-8') as N:
            ordem = json.load(N)
    except (FileNotFoundError, json.JSONDecodeError):
        ordem = []
       
    while resposta != 0:
        menu()
        resposta = int(input('Selecione a Opção'))
        if resposta == 1:
            criar(ordem)
            salvar(ordem)
        elif resposta == 2:
            listar(ordem)
            salvar(ordem)
        elif resposta == 3:
            buscar(ordem)
            salvar(ordem)
        elif resposta == 4:
            editar(ordem)
            salvar(ordem)
        elif resposta == 5:
            excluir(ordem)
            salvar(ordem)
        elif resposta == 6:
            teste(ordem, criaturas)
            salvar(ordem)
        elif resposta == 7:
            batalha(criaturas)
        elif resposta == 0:
            salvar(ordem)
            print('Salvando fichas...')
            break
        else: print('Opção Invalida')
inicio()            
    

    
