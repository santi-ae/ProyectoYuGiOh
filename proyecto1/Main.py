import random 
import CartaMounstro, CartaMagica, CartaTrampa 
import Jugador 
import Deckbuilder 
import Tablero
import TipoAtributo
import TipoMounstro

def main():
    cartas_disponibles = Deckbuilder.leer_cartas_desde_archivo('cartas.txt') 
    # Crear jugadores 
    a=input("Ingresa tu nombre")
    jugador = Jugador(a) 
    maquina = Jugador("Máquina")
    #Crear los decks de el jugador y la maquina ellos solo tienen 30 cartas por deck
    jugador.deck = Deckbuilder.crear_deck(cartas_disponibles) 
    maquina.deck = Deckbuilder.crear_deck(cartas_disponibles)
    
    # Cada jugador empieza con 5 cartas 
    jugador.mano = [jugador.deck.pop() for _ in range(5)] 
    maquina.mano = [maquina.deck.pop() for _ in range(5)]
    
    #Creamos una instancia de tablero
    tablero = Tablero()
    #mostramos la mano al jugadro
    
    i=0           
    turno_jugador = random.choice([True, False]) 
    if turno_jugador: 
        print("\nEl jugador comienza primero.")
    
    else: 
        print("\nLa máquina comienza primero.")

    if turno_jugador is True:
        turno_actual = jugador.nombre
    else:
        turno_actual="maquina"
    
    while jugador.puntos>0 and maquina.puntos>0:
        
        if turno_actual == "Jugador" and i==0: 
            print("\nTurno del Jugador") 
            carta_robada = jugador.robar_carta() 
            if carta_robada: 
                print(f"El jugador robó la carta: {carta_robada.nombre}") 
        
            else: 
                print("El jugador no puede robar más cartas, su deck está vacío.")
            
            print("Mano del Jugador:")
            for carta in jugador.mano: 
                if isinstance(CartaMounstro):
                    print(f"{carta.nombre}  {carta.descripcion} {carta.ataque} {carta.defensa} {carta.tipoMounstro} {carta.atributo}")
            
                elif isinstance(CartaMagica):
                    print(f"{carta.nombre} {carta.descripcion}{carta.aumento} {carta.estadistica}")
            
                elif isinstance(CartaTrampa):
                    print(f"{carta.nombre} {carta.descripcion}{carta.atributo} ")


            
