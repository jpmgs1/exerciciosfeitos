#Lista 01 - Questão 15

salario = float(input("Digite o salário de João: "))
conta1 = float(input("Digite o valor da primeira conta: "))
conta2 = float(input("Digite o valor da segunda conta: "))
multa = 0.02  
conta1_com_multa = conta1 + (conta1 * multa)
conta2_com_multa = conta2 + (conta2 * multa)

total_pago = conta1_com_multa + conta2_com_multa

saldo_restante = salario - total_pago

print(f"João pagará R${conta1_com_multa:.2f} na primeira conta (com multa).")
print(f"João pagará R${conta2_com_multa:.2f} na segunda conta (com multa).")
print(f"Total gasto com contas: R${total_pago:.2f}")
print(f"Saldo restante do João: R${saldo_restante:.2f}")