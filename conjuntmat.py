def menu():
    print(f"{' CONJUNTOS MATEMÁTICOS ':=^50}")
    print("1. Criar novo conjunto")
    print("2. Adicionar elemento a um conjunto")
    print("3. Remover elemento de um conjunto")
    print("4. Mostrar todos os conjuntos")
    print("5. Apagar um conjunto")
    print("6. União de dois conjuntos")
    print("7. Interseção de dois conjuntos")
    print("0. Sair")
    print("=" * 50)

conjuntos = [] 

def criar_conjunto():
    print(f"{' CRIAR CONJUNTO ':=^50}")
    while True:
        nome = input(">> Nome do novo conjunto (ou 'sair' para voltar): ")
        if nome == "sair":
            break
        for c in conjuntos:
            if c[0] == nome:
                print(">> Já existe um conjunto com esse nome.")
                break
        else:
            conjuntos.append([nome, []])
            print(f">> Conjunto '{nome}' criado com sucesso.")

def adicionar_elemento():
    print(f"{' ADICIONAR ELEMENTO ':=^50}")
    nome = input(">> Nome do conjunto (ou 'sair' para voltar): ")
    if nome == 'sair':
        return
    for c in conjuntos:
        if c[0] == nome:
            while True:
                elemento = input(">> Digite o elemento (digite 'sair' para voltar): ")
                if elemento == 'sair':
                    return
                if elemento in c[1]:
                    print(">> Elemento já está no conjunto.")
                else:
                    c[1].append(elemento)
                    print(f">> Elemento '{elemento}' adicionado.")
            return
    print(">> Conjunto não encontrado.")

def remover_elemento():
    print(f"{' REMOVER ELEMENTO ':=^50}")
    while True:
        nome = input(">> Nome do conjunto (digite 'sair' para voltar): ")
        if nome == 'sair':
            break
        for c in conjuntos:
            if c[0] == nome:
                while True:
                    elemento = input(">> Elemento para remover (digite 'sair' para voltar): ")
                    if elemento == 'sair':
                        break
                    if elemento in c[1]:
                        c[1].remove(elemento)
                        print(f">> Elemento '{elemento}' removido.")
                    else:
                        print(">> Elemento não encontrado.")
                break
        else:
            print(">> Conjunto não encontrado.")

def mostrar_conjuntos():
    print(f"{' CONJUNTOS CRIADOS ':=^50}")
    if len(conjuntos) == 0:
        print(">> Nenhum conjunto criado.")
    else:
        for c in conjuntos:
            print(f">> {c[0]:.<20} {c[1]}")

def apagar_conjunto():
    print(f"{' APAGAR CONJUNTO ':=^50}")
    nome = input(">> Nome do conjunto para apagar: ")
    for c in conjuntos:
        if c[0] == nome:
            conjuntos.remove(c)
            print(f">> Conjunto '{nome}' apagado.")
            return
    print(">> Conjunto não encontrado.")

def unir_conjuntos():
    print(f"{' UNIÃO DE CONJUNTOS ':=^50}")
    nome1 = input(">> Primeiro conjunto: ")
    nome2 = input(">> Segundo conjunto: ")
    c1 = []
    c2 = []
    encontrou_c1 = encontrou_c2 = 0
    for c in conjuntos:
        if c[0] == nome1:
            c1 = c[1]
            encontrou_c1 = 1
        if c[0] == nome2:
            c2 = c[1]
            encontrou_c2 = 1
    if not (encontrou_c1 and encontrou_c2):
        print(">> Um ou ambos os conjuntos não foram encontrados.")
        return
    uniao = list(c1)
    for item in c2:
        if item not in uniao:
            uniao.append(item)
    print(f">> União entre '{nome1}' e '{nome2}': {uniao}")

def interseccao_conjuntos():
    print(f"{' INTERSEÇÃO DE CONJUNTOS ':=^50}")
    nome1 = input(">> Primeiro conjunto: ")
    nome2 = input(">> Segundo conjunto: ")
    c1 = []
    c2 = []
    encontrou_c1 = encontrou_c2 = 0
    for c in conjuntos:
        if c[0] == nome1:
            c1 = c[1]
            encontrou_c1 = 1
        if c[0] == nome2:
            c2 = c[1]
            encontrou_c2 = 1
    if not (encontrou_c1 and encontrou_c2):
        print(">> Um ou ambos os conjuntos não foram encontrados.")
        return
    intersecao = [item for item in c1 if item in c2]
    print(f">> Interseção entre '{nome1}' e '{nome2}': {intersecao}")

def main():
    while True:
        menu()
        opcao = input(">> Escolha uma opção: ")
        if opcao == '1':
            criar_conjunto()
        elif opcao == '2':
            adicionar_elemento()
        elif opcao == '3':
            remover_elemento()
        elif opcao == '4':
            mostrar_conjuntos()
        elif opcao == '5':
            apagar_conjunto()
        elif opcao == '6':
            unir_conjuntos()
        elif opcao == '7':
            interseccao_conjuntos()
        elif opcao == '0':
            print(">> Bye Bye ;)")
            break
        else:
            print(">> Opção invalida.")
 main()