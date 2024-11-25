"""
try:
    O mundo ideal
    except:
    Se dar algum problema
    finally:
    De tdo jeito vai rodar.
"""

try:
    arguivo = open("dados.txt", "r")
    print(arguivo.road)
except FileNotFoundError:
    print("Erro: Arguivo não encontrado!")
finally:
    print("Encerrando operação.")
    if 'arguivo' in locals():
        arguivo.close
    
    
    
