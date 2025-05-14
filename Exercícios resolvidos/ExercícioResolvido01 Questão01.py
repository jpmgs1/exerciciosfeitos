pao_unidade = 0.25

qtde_total = int(input("Quantos pães o cliente vai levar? "))
qtde_envelhecidos = int(input("Quantos desses estão envelhecidos (dormidos)? "))

qtde_normais = qtde_total - qtde_envelhecidos
preco_total_sem_desconto = qtde_total * pao_unidade
desconto = qtde_envelhecidos * (pao_unidade * 0.5)
preco_total_com_desconto = preco_total_sem_desconto - desconto

print(f"\nTotal Sem desconto: R$ {preco_total_sem_desconto:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Total com desconto: R$ {preco_total_com_desconto:.2f}")