from generar_cartas import generar_cartas_monstruo, guardar_cartas, generar_cartas_magicas, generar_cartas_trampa

if __name__ == "__main__":
    cartas_monstruo = generar_cartas_monstruo()
    cartas_trampa = generar_cartas_trampa()
    cartas_magicas = generar_cartas_magicas()

    guardar_cartas(cartas_monstruo, "cartas_monstruo.txt")
    guardar_cartas(cartas_trampa, "cartas_trampa.txt")
    guardar_cartas(cartas_magicas, "cartas_magicas.txt")

    print("Se han guardado las cartas en sus archivos correspondientes")
