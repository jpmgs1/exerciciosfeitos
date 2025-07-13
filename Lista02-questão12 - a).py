#João Paulo - Redes de Computadores 1v
def calcular_preco():
    print("Programa de Cálculo de Preço com Desconto")
    print(42 *"-")

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
        else:  # 31-40
            preco_unitario = 30.00

        preco_total = preco_unitario * quantidade

        if preco_total <= 250.00:
            desconto = 0.05
        elif 250.00 < preco_total <= 500.00:
            desconto = 0.10
        else:
            desconto = 0.15

        valor_com_desconto = preco_total * (1 - desconto)

        print("\nResumo da Compra:")
        print(f"Código do produto: {codigo}")
        print(f"Quantidade: {quantidade}")
        print(f"Preço unitário: R$ {preco_unitario:.2f}")
        print(f"Preço total sem desconto: R$ {preco_total:.2f}")
        print(f"Desconto aplicado: {desconto*100:.0f}%")
        print(f"Valor final com desconto: R$ {valor_com_desconto:.2f}")

    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos.")

calcular_preco()