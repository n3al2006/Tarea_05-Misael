# Importamos la libreria random
import random

# Posibles casos de maquina y lo que escribas
turnoMaquina = ["Piedra", "Papel", "Tijera"]
turnoHumano = ["Piedra", "Papel", "Tijera"]

while True:
    num = random.randrange(0,3)
    print("================== Bienvenido al juego de Piedra | Papel | Tijera ==============")
    print()
    a = input("Escribe Piedra, Papel o Tijera: ")
    print(f"Maquina dice: {turnoMaquina[num].lower()}")
    
    # Aqui hacemos las validaciones a posibles casos donde ganaría la maquina
    
    if turnoMaquina[num].lower() == turnoMaquina[0].lower() and a.lower() == turnoHumano[2].lower():
        print("========== MAQUINA GANA =============")
        print("")
        break
    
    elif turnoMaquina[num].lower() == turnoMaquina[1].lower() and a.lower() == turnoHumano[0].lower():
        print("========== MAQUINA GANA =============")
        print("")
        break
        
    elif turnoMaquina[num].lower() == turnoMaquina[2].lower() and a.lower() == turnoHumano[1].lower():
        print("========== MAQUINA GANA =============")
        print("")
        break
        
    # Validación a posible empate
    elif turnoMaquina[num].lower() == a.lower() :
        print("========== EMPATE =============")
        break
    
    else:
        print("============ GANASTE ==============")
        break
        
