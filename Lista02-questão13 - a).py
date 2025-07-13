#João Paulo - Redes de Computadores 1v
def calcular_aumento(preco, categoria):
    categoria = categoria.lower()
    
    if preco <= 25:
        if categoria == "limpeza":
            percentual = 5
        elif categoria == "alimentação":
            percentual = 8
        elif categoria == "vestuário":
            percentual = 10
        else:
            percentual = 0
    else:
        if categoria == "limpeza":
            percentual = 12
        elif categoria == "alimentação":
            percentual = 15
        elif categoria == "vestuário":
            percentual = 18
        else:
            percentual = 0
    
    valor_aumento = preco * percentual / 100
    return percentual, valor_aumento

def main():
    preco = float(input("Digite o preço do produto: R$ "))
    categoria = input("Digite a categoria (Limpeza, Alimentação ou Vestuário): ")
    situacao = input("Digite a situação (R - precisa de refrigeração, S - não precisa): ").upper()
    
    percentual, aumento = calcular_aumento(preco, categoria)
    novo_preco = preco + aumento
    
    print("\nResultados:")
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Categoria: {categoria.capitalize()}")
    print(f"Situação: {'Precisa de refrigeração' if situacao == 'R' else 'Não precisa de refrigeração'}")
    print(f"Percentual de aumento: {percentual}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Novo preço: R$ {novo_preco:.2f}")

if __name__ == "__main__":
    main()