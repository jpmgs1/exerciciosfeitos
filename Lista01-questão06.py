#Lista 01 - Questão 06

preco = float(input("Digite o preço do produto: R$ "))

desconto = preco * 0.10

novo_preco = preco - desconto

print("O valor do desconto é: R$ {:.2f}".format(desconto))
print("Preço com 10% de desconto é: R$ {:.2f}".format(novo_preco))
