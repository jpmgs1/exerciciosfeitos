#João Paulo - Redes de Computadores 1v
def calcular_peso_ideal(altura, sexo):
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        raise ValueError("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")
    return peso_ideal

def main():
    try:
        altura = float(input("Digite a sua altura em metros. EX: 1.70 :"))
        if altura < 0:
            print("Erro: A altura não pode ser um valor negativo.")
            return
        sexo = input("Digite o seu sexo (M-masculino ou F-feminino): ").upper()

        peso_ideal = calcular_peso_ideal(altura, sexo)
        print(f"O seu peso ideal é: {peso_ideal:.2f} kg")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()