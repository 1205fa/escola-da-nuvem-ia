"""
1: 4.00,
2: 4.50,
3: 5.00,
4: 2.00,
5: 1.50

"""

codigo, quantidade = map(int,
                             input("Digite o codigo do produto e a quantidade (seaptados por espaços): ").split())

precos = {
        1: 4.00,
        2: 4.50,
        3: 5.00,
        4: 2.00,
        5: 1.50
    }
    
    
    
total = precos[codigo] * quantidade
    
print(f"total: R$ {total:.2f}")
    
 