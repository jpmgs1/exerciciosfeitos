#João Paulo - Redes de Computadores 1v
def calcular_credito(saldo_medio):
  if saldo_medio > 400.00:
    percentual_credito = 0.30
  elif saldo_medio >= 301.00 and saldo_medio <= 400.00:
    percentual_credito = 0.25
  elif saldo_medio >= 201.00 and saldo_medio <= 300.00:
    percentual_credito = 0.20
  else:
    percentual_credito = 0.10

  valor_credito = saldo_medio * percentual_credito
  return f"Saldo médio: R$ {saldo_medio:.2f}\nValor do crédito: R$ {valor_credito:.2f}"
saldo_cliente = float(input("Digite o saldo médio do cliente: R$ "))

resultado_credito = calcular_credito(saldo_cliente)
print(resultado_credito)