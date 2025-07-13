#João Paulo - Redes de Computadores 1v
def calcular_desconto():
    print("Cálculo de Desconto na Nota Fiscal")
    print(35 *"-")

    try:
        codigo = int(input("Digite o código do produto (1-40): "))
        quantidade = int(input("Digite a quantidade comprada: "))

        if codigo < 1 or codigo > 40:
            print("Erro: Código de produto inválido. Digite um valor entre 1 e 40.")
            return

        if 1 <= codigo <= 10:
            preco_unitario = 10.00
        elif 11 <= codigo <= 20:
            preco_unitario = 15.00
        elif 21 <= codigo <= 30:
            preco_unitario = 20.00
        else:
            preco_unitario = 30.00

        preco_total = preco_unitario * quantidade

        if preco_total <= 250.00:
            percentual = 5
            desconto = preco_total * 0.05
        elif preco_total <= 500.00:
            percentual = 10
            desconto = preco_total * 0.10
        else:
            percentual = 15
            desconto = preco_total * 0.15

        print("\nResumo da Compra:")
        print(f"Preço unitário: R$ {preco_unitario:.2f}")
        print(f"Quantidade: {quantidade}")
        print(f"Preço total: R$ {preco_total:.2f}")
        print(f"Desconto ({percentual}%): R$ {desconto:.2f}")
        print(f"Valor final: R$ {preco_total - desconto:.2f}")

    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos.")

calcular_desconto()
