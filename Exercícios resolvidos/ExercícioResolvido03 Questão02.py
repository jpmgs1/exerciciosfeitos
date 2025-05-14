velocidade = float(input("Digite a velocidade do carro em km/h: "))

if velocidade > 80:
  excesso = velocidade - 80
  multa = 150 + (excesso * 5)
  print("Você foi multado!")
  print(f"O valor da multa é de R$ {multa:.2f}")
else:
  print("Você está dentro do limite de velocidade.")