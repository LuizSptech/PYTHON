import random
import time

# 1. Definindo o ambiente e os estímulos
estados_sensor = ["sujeira", "obstáculo", "caminho_limpo"]

def ler_sensor():
    # Simula o robô detectando o ambiente a cada segundo
    time.sleep(1)
    return random.choice(estados_sensor)

# 2, 3 e 4. O loop da IA aplicando as regras reativas
def executar_ia_reativa():
    print("Iniciando IA Reativa... (Pressione Ctrl+C para parar)")
    
    try:
        while True:

            estimulo = ler_sensor()
            print(f"\n[Sensor detectou]: {estimulo}")
            
            # Regras de produção (Se / Então)
            if estimulo == "sujeira":
                print("-> [Ação]: Aspirar e limpar.")
            elif estimulo == "obstáculo":
                print("-> [Ação]: Girar 90 graus para a direita.")
            elif estimulo == "caminho_limpo":
                print("-> [Ação]: Seguir em frente.")
                
    except KeyboardInterrupt:
        print("\nIA finalizada.")

# Executar o robô
executar_ia_reativa()
