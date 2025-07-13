#João Paulo - Redes de Computadores 1v
def mostrar_preco_unitario():
    print("Consulta de Preço Unitário - Tabela")
    print(37 *"-")

    try:
        codigo = int(input("Digite o código do produto (1-40): "))

        if codigo < 1 or codigo > 40:
            print("Erro: Código de produto inválido. Digite um valor entre 1 e 40.")
            return

        if 1 <= codigo <= 10:
            preco = 10.00
            faixa = "1 a 10"
        elif 11 <= codigo <= 20:
            preco = 15.00
            faixa = "11 a 20"
        elif 21 <= codigo <= 30:
            preco = 20.00
            faixa = "21 a 30"
        else:  # 31-40
            preco = 30.00
            faixa = "31 a 40"

        print(f"\nProduto código {codigo} (faixa {faixa})")
        print(f"Preço unitário: R$ {preco:.2f}")

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")

mostrar_preco_unitario()