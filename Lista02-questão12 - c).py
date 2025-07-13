#João Paulo - Redes de Computadores 1v
def calcular_preco_total():
    print("Cálculo do Preço Total da Nota")
    print(32 *"-")

    try:
        codigo = int(input("Digite o código do produto (1-40): "))
        quantidade = int(input("Digite a quantidade comprada: "))

        if codigo < 1 or codigo > 40:
            print("Erro: Código de produto inválido. Digite um valor entre 1 e 40.")
            return

        if 1 <= codigo <= 10:
            preco_unitario = 10.00
            faixa = "1 a 10"
        elif 11 <= codigo <= 20:
            preco_unitario = 15.00
            faixa = "11 a 20"
        elif 21 <= codigo <= 30:
            preco_unitario = 20.00
            faixa = "21 a 30"
        else:
            preco_unitario = 30.00
            faixa = "31 a 40"

        preco_total = preco_unitario * quantidade

        print("\nResumo da Compra:")
        print(f"Código do produto: {codigo} (faixa {faixa})")
        print(f"Preço unitário: R$ {preco_unitario:.2f}")
        print(f"Quantidade comprada: {quantidade}")
        print(f"Preço total da nota: R$ {preco_total:.2f}")

    except ValueError:
        print("Erro: Por favor, digite valores numéricos válidos.")
calcular_preco_total()
