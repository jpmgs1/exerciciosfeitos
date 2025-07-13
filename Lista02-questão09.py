#João Paulo - Redes de Computadores 1v
def calcular_novo_preco(preco_original):
    if preco_original <= 50:
        aumento = 0.05  # 5% de aumento
    elif preco_original <= 100:
        aumento = 0.10  # 10% de aumento
    else:
        aumento = 0.15  # 15% de aumento
    
    novo_preco = preco_original * (1 + aumento)
    return novo_preco
def classificar_produto(preco):
    if preco <= 80:
        return "Barato"
    elif preco <= 120:
        return "Normal"
    elif preco <= 200:
        return "Caro"
    else:
        return "Muito Caro"
def main():
    print("Calculadora de Preços de Produtos")
    print("---------------------------------")
    
    try:
        preco = float(input("Digite o preço do produto: R$ "))
        
        if preco < 0:
            print("Erro: O preço não pode ser negativo!")
            return
        novo_preco = calcular_novo_preco(preco)
        print("\nResultado:")
        print(f"Preço original: R$ {preco:.2f}")
        print(f"Novo preço: R$ {novo_preco:.2f}")
        print(f"Classificação: {classificar_produto(novo_preco)}")
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido!")
if __name__ == "__main__":
    main()