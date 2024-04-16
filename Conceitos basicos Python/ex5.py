# Escreva um programa que calcule o salário líquido. 
# Lembrando de declarar o salário bruto e o percentual de desconto 
# do Imposto de Renda. ●Renda até R$1.903,98:isento de imposto de renda;
# Renda entre R$1.903,99 e R$2.826,65:alíquota de 7,5%;
# Renda entre R$2.826,66 e R$3.751,05:alíquota de 15%;
# Renda entre R$3.751,06 e R$4.664,68:alíquota de 22,5%;
# Renda acima de R$4.664,68:alíquota máxima de 27,5%


salario_bruto = float(input('Informe seu salario bruto :'))

if salario_bruto <= 1903.98:
    aliquota = 0
elif salario_bruto <= 2826.65:
    aliquota = 0.075
elif salario_bruto <= 3751.05:
    aliquota = 0.15
elif salario_bruto <= 4664.68:
    aliquota = 0.225
else:
    aliquota = 0.275
    
salario_liquido = salario_bruto - (salario_bruto * aliquota)

print(f'O salario liquido eh R${salario_liquido:.2f}')