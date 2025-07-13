## Lista 04 - João Paulo - 1v - redes
produtos = []
precos = []

print("Cadastro de Produtos (digite 'sair' para encerrar)\n")

while True:
    nome = input("Nome do produto: ").strip()
    if nome.lower() == 'sair':
        break
    
    while True:
        try:
            preco = float(input("Preço do produto (R$): "))
            if preco >= 0:
                break
            else:
                print("O preço não pode ser negativo.")
        except ValueError:
            print("Digite um valor numérico válido.")
    
    produtos.append(nome)
    precos.append(preco)

if not produtos:
    print("\nNenhum produto cadastrado.")
else:
    indice_caro = precos.index(max(precos))
    indice_barato = precos.index(min(precos))
    
    print("\n--- Antes do reajuste ---")
    print(f"Mais caro: {produtos[indice_caro]} - R$ {precos[indice_caro]:.2f}")
    print(f"Mais barato: {produtos[indice_barato]} - R$ {precos[indice_barato]:.2f}")

    precos_reajustados = []
    print("\n--- Preços reajustados ---")
    for i in range(len(produtos)):
        if precos[i] <= 20:
            novo_preco = precos[i] * 1.10
        else:
            novo_preco = precos[i] * 1.05
        precos_reajustados.append(novo_preco)
        print(f"{produtos[i]}: R$ {novo_preco:.2f}")

    indice_caro_novo = precos_reajustados.index(max(precos_reajustados))
    indice_barato_novo = precos_reajustados.index(min(precos_reajustados))
    
    print("\n--- Após reajuste ---")
    print(f"Mais caro: {produtos[indice_caro_novo]} - R$ {precos_reajustados[indice_caro_novo]:.2f}")
    print(f"Mais barato: {produtos[indice_barato_novo]} - R$ {precos_reajustados[indice_barato_novo]:.2f}")
