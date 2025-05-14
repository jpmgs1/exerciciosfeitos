consumo = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R para residencial, I para industrial, C para comercial): ").upper()

preco = 0.0

if tipo_instalacao == 'R':
    if consumo <= 500:
        preco = consumo * 0.40
    else:
        preco = consumo * 0.65
elif tipo_instalacao == 'C':
    if consumo <= 1000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
elif tipo_instalacao == 'I':
    if consumo <= 5000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
else:
    print("Tipo de instalação inválido.")

if preco > 0:
    print(f"O preço a pagar pelo fornecimento de energia elétrica é de R$ {preco:.2f}")