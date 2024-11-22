nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário do colaborador: "))
vendas = float(input("Digite o valor total das vendas: "))
comissao = float(input("Digite o valor da comisão: "))

total = salario_fixo + (vendas * comissao)

print(f"O valor a receber do colaborador {nome} é de  R$ {total:.2f}")