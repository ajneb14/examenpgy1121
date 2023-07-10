from os import system
system("cls")


asientos=list(range(1,101))

def menu():
       while True:
            print("""
            *****CONCIERTO MICHAEL JAM*****
                1. Comprar entradas
                2. Mostrar ubicaciones disponibles
                3. Ver listado de asistentes
                4. Mostrar ganancias totales
                5. Salir
                """)
            op=input("Ingrese una opcion \n")
            match op:
                case "1":
                      menu()
       























































