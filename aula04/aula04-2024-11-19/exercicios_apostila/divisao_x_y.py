n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
if y == 0 or x < 0 or y < 0:
    print("Divisao impossivel")
else:
    print(f"{x / y:.1f}")
    