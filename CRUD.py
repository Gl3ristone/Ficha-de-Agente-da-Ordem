import json
def menu():
    print('''Bem-vindo à FAO
Ficha dos Agentes da Ordem
Opções:
1. Criar
2. Listar
3. Buscar
4. Editar
5. Excluir
0. Sair
''')
def salvar(ordem, filename = "dados.json"):
    with open(filename, 'w') as f:
        json.dump(ordem, f)
def criar(ordem):
    agente = {
        'id': input('ID do agente: '),
        'nome': input('Nome do Agente: '),
        'origem': input('Origem: '),
        'classe': input('Classe: '),
        'trilha': input('Trilha da Classe: '),
        'nex': int(input('Nível de Exposição: '))
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
            print(f"ID: {agente['id']}, Nome: {agente['nome']}, Origem: {agente['origem']}, "
                  f"Classe: {agente['classe']}, Trilha: {agente['trilha']}, Nex: {agente['nex']}%")
            return
    print(f'Nenhum agente com ID: {buscavel} encontrado')
def editar(ordem):
    buscavel = input('ID do agente desejado: ')
    for agente in ordem:
        if agente['id'] == buscavel:
            print(f"ID: {agente['id']}, Nome: {agente['nome']}, Origem: {agente['origem']}, "
                  f"Classe: {agente['classe']}, Trilha: {agente['trilha']}, Nex: {agente['nex']}%")
            
            editor = {
                'id': input('Novo ID do agente: '),
                'nome': input('Novo nome do agente: '),
                'origem': input('Nova origem: '),
                'classe': input('Nova classe: '),
                'trilha': input('Nova trilha da classe: '),
                'nex': int(input('Novo nível de exposição: '))
            }

            agente.update(editor)
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
def inicio():
    resposta = 1
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
        elif resposta == 2:
            listar(ordem)
        elif resposta == 3:
            buscar(ordem)
        elif resposta == 4:
            editar(ordem)
        elif resposta == 5:
            excluir(ordem)
        elif resposta == 0:
            salvar(ordem)
            print('Salvando fichas...')
            break
        else: print('Opção Invalida')
inicio()            
    
    
