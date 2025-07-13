#João Paulo - Redes de Computadores 1v
def identificar_procedencia():
    print("Programa de Identificação de Produtos")
    print(37 *"-")

    try:
        codigo = int(input("Digite o código de origem do produto: "))

        if codigo == 1:
            procedencia = "Sul"
        elif codigo == 2:
            procedencia = "Norte"
        elif codigo == 3:
            procedencia = "Leste"
        elif codigo == 4:
            procedencia = "Oeste"
        elif codigo in [5, 6] or 21 <= codigo <= 30:
            procedencia = "Nordeste"
        elif codigo in [7, 8, 9]:
            procedencia = "Sudeste"
        elif 10 <= codigo <= 20:
            procedencia = "Centro-oeste"
        else:
            procedencia = "Código inválido ou procedência não especificada"

        print(f"Região do produto com código {codigo} é: {procedencia}")

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")

# Executar o programa
identificar_procedencia()