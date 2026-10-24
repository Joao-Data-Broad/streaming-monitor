
def analizar_logs(nombre_archivo):
    errores = 0
    advertencias = 0
    eventos = 0

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()

                if not linea:
                    continue

                eventos += 1

                if "ERROR" in linea:
                    errores += 1
                    print("ALERTA:", linea)

                elif "WARNING" in linea:
                    advertencias += 1

        print("\n--- RESUMEN ---")
        print("Eventos analizados:", eventos)
        print("Errores:", errores)
        print("Advertencias:", advertencias)

    except FileNotFoundError:
        print("ERROR: no se encontró el archivo:", nombre_archivo)


analizar_logs("logs/streaming.log")
