n = int(input())# ele pediu 7 casos de teste
#entre o valor x e y
#soma todos os impares entre x e y

"""
Se x = 7
y = 4

7,8,9,10,11
"""

for _ in range(n):  #esse valor de variavel_(mantém o tipo e descarta a variável)
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
        
    soma = sum(i for i in range(x + 1, y) if i % 2 != 0)#é impar
    print(soma)
    