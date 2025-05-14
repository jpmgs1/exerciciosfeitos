nome_mes = input("Digite o nome de um mês: ").lower()

if nome_mes == "fevereiro":
  print("O mês de fevereiro tem 28 ou 29 dias.")
elif nome_mes in ["janeiro", "março", "maio", "julho", "agosto", "outubro", "dezembro"]:
  print("Este mês tem 31 dias.")
elif nome_mes in ["abril", "junho", "setembro", "novembro"]:
  print("Este mês tem 30 dias.")
else:
  print("Nome de mês inválido.")