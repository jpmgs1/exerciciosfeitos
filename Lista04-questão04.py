## Lista 04 - João Paulo - 1v - redes
lista1 = []
lista2 = []

tamanho1 = int(input("Digite o número de nomes para a Lista 1: "))
print("Digite os nomes para a Lista 1:")
for i in range(tamanho1):
    nome = input(f"{i+1}º nome: ")
    lista1.append(nome)

tamanho2 = int(input("\nDigite o número de nomes para a Lista 2: "))
print("Digite os nomes para a Lista 2:")
for i in range(tamanho2):
    nome = input(f"{i+1}º nome: ")
    lista2.append(nome)

lista_unida = lista1 + lista2

lista_unida.sort()

print("\nLista unida e ordenada:")
for nome in lista_unida:
    print(nome)
