#João Paulo - Redes de Computadores 1v
def calcular_nota_fiscal():
    print("\nSISTEMA DE CÁLCULO DE NOTA FISCAL")
    print(34 * "-")

    try:
        codigo = int(input("Digite o código do produto (1-40): "))
        quantidade = int(input("Digite a quantidade comprada: "))

        if codigo < 1 or codigo > 40:
            print("\nERRO: Código deve estar entre 1 e 40")
            return

        if 1 <= codigo <= 10:
            preco_unitario = 10.00
            faixa = "1-10"
        elif 11 <= codigo <= 20:
            preco_unitario = 15.00
            faixa = "11-20"
        elif 21 <= codigo <= 30:
            preco_unitario = 20.00
            faixa = "21-30"
        else:  # 31-40
            preco_unitario = 30.00
            faixa = "31-40"

        preco_total = preco_unitario * quantidade

        if preco_total <= 250:
            percentual = 5
        elif preco_total <= 500:
            percentual = 10
        else:
            percentual = 15

        desconto = preco_total * percentual / 100
        preco_final = preco_total - desconto

        print("\n" + "=" * 42)
        print("NOTA FISCAL - Aula Programação".center(42))
        print("=" * 42)
        print(f"Produto (Cód. {codigo}, Faixa {faixa})")
        print(f"{'Preço unitário:':<20} R$ {preco_unitario:>8.2f}")
        print(f"{'Quantidade:':<20} {quantidade:>10}")
        print("-" * 42)
        print(f"{'Subtotal:':<20} R$ {preco_total:>8.2f}")
        print(f"{f'Desconto ({percentual}%):':<20} R$ {desconto:>8.2f}")
        print("=" * 42)
        print(f"{'TOTAL A PAGAR:':<20} R$ {preco_final:>8.2f}".upper())
        print("=" * 42)

    except ValueError:
        print("\nERRO: Digite apenas números válidos")

if __name__ == "__main__":
    calcular_nota_fiscal()