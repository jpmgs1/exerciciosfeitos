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

def calcular_imposto(preco, categoria, situacao):
    """
    Calcula o imposto extra com base na categoria e situação.
    Retorna o percentual e o valor do imposto.
    """
    categoria = categoria.lower()
    situacao = situacao.upper()
    
    if categoria == "alimentação" or situacao == "R":
        percentual = 5
    else:
        percentual = 8
    
    valor_imposto = preco * percentual / 100
    return percentual, valor_imposto

def main():
    preco = float(input("Digite o preço do produto: R$ "))
    categoria = input("Digite a categoria (Limpeza, Alimentação ou Vestuário): ")
    situacao = input("Digite a situação (R - precisa de refrigeração, S - não precisa): ").upper()
    
    percentual_aumento, aumento = calcular_aumento(preco, categoria)
    preco_com_aumento = preco + aumento
    
    percentual_imposto, imposto = calcular_imposto(preco, categoria, situacao)
    preco_final = preco_com_aumento + imposto
    
    print("\n--- RESUMO DO CÁLCULO ---")
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Categoria: {categoria.capitalize()}")
    print(f"Situação: {'Precisa de refrigeração (R)' if situacao == 'R' else 'Não precisa de refrigeração (S)'}")
    
    print("\n--- AUMENTO APLICADO ---")
    print(f"Percentual de aumento: {percentual_aumento}%")
    print(f"Valor do aumento: R$ {aumento:.2f}")
    print(f"Preço após aumento: R$ {preco_com_aumento:.2f}")
    
    print("\n--- IMPOSTO EXTRA ---")
    print(f"Percentual de imposto: {percentual_imposto}%")
    print(f"Valor do imposto: R$ {imposto:.2f}")
    
    print("\n--- PREÇO FINAL ---")
    print(f"Preço final (original + aumento + imposto): R$ {preco_final:.2f}")

if __name__ == "__main__":
    main()