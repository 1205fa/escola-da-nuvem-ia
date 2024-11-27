"""
CIDADE A(SETE LAGOAS) E CIDADE(OSVALDO CRUZ)
ÍNDICE DE CRESCIMENTO (G1 E G2)
"""

def calculo_anos(PA, PB, G1, G2):
    """
    FUNÇÃO QUE CALCULA QUANTOS ANOS A POPULAÇÃO DE (A) LEVA PARA ULTRAPASSAR A(B)
    SE ULTRAPASSAR 100 ANOS, "MAIS DE 1 SÉCULO"
    
    """
    
    anos = 0
    
    while PA <= PB:
        #Incremento dos anos de forma proporcional mulTIPLICANDO A PORCENTAGEM DE G (ÍNDICE)
        PA += int(PA *(G1 / 100))
        PB += int(PB *(G2 / 100))
        anos += 1
        
        if anos > 100:
            return "Mais de 1 século" #DENTRO DO ÍF
        
    return f"{anos} anos." 
    
def main():
    try:
        
        T = int(input())  #números de teste
        
        #[100 400 500 100]
        for i in range (T):
            PA, PB, G1, G2 = map(float, input(). split()) 
            PA, PB = int(PA), int(PB) #Convertendo cidades para inteiro
            
            resultado = calculo_anos(PA, PB, G1,G2)
            
            
            print(resultado)
        
    except ValueError as ve:
        print(f"Erro {ve}")
        
        
if __name__ == "__main__":
    main()