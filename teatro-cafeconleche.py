compradores = {}
stock_funcion1 = 150
stock_funcion2 = 180
vendidas_funcion1 = 0
vendidas_funcion2 = 0


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\nTOTEM AUTOATENCIÓN CAFECONLECHE")
    print("1.- Comprar entrada a Cats.")
    print("2.- Cambio de función.")
    print("3.- Mostrar stock de funciones.")
    print("4.- Salir.")

def comprar_entrada():
    """Permite la compra de una entrada verificando todas las condiciones"""
    global compradores, stock_funcion1, stock_funcion2, vendidas_funcion1, vendidas_funcion2
    
    print("\n-- Comprar entrada a Cats --")
    
    nombre = input("Nombre del comprador: ").strip()
    
    if not nombre:
        print("Error: el nombre no puede estar vacío.")
        return
    
    if nombre in compradores:
        print(f"Error: el comprador {nombre} ya tiene una entrada.")
        return
    
    print("Seleccione función:")
    print(f"1. Cats Día Viernes ({stock_funcion1 - vendidas_funcion1} entradas)")
    print(f"2. Cats Día Sábado ({stock_funcion2 - vendidas_funcion2} entradas)")
    
    funcion = input("Función (1 ó 2): ")
    
    if funcion not in ['1', '2']:
        print("Error: opción de función inválida.")
        return
    
    if funcion == '1':
        if vendidas_funcion1 < stock_funcion1:
            compradores[nombre] = 1
            vendidas_funcion1 += 1
            print(f"Entrada registrada en función 1! Stock restantes:")
            print(f"Función 1 (Viernes): {stock_funcion1 - vendidas_funcion1}")
            print(f"Función 2 (Sábado): {stock_funcion2 - vendidas_funcion2}")
        else:
            print("Error: no hay entradas disponibles para la función 1.")
    else:
        if vendidas_funcion2 < stock_funcion2:
            compradores[nombre] = 2
            vendidas_funcion2 += 1
            print(f"Entrada registrada en función 2! Stock restantes:")
            print(f"Función 1 (Viernes): {stock_funcion1 - vendidas_funcion1}")
            print(f"Función 2 (Sábado): {stock_funcion2 - vendidas_funcion2}")
        else:
            print("Error: no hay entradas disponibles para la función 2.")


def cambio_funcion():
    """Permite cambiar de función a un comprador existente"""
    global compradores, vendidas_funcion1, vendidas_funcion2
    
    print("\n-- Cambio de función --")
    
    nombre = input("Nombre del comprador: ")
    
    if nombre not in compradores:
        print("Error: comprador no encontrado.")
        return
    
    funcion_actual = compradores[nombre]
    funcion_nueva = 2 if funcion_actual == 1 else 1
    
    confirmacion = input(f"Cambiar de función {funcion_actual} a {funcion_nueva}? (S/N): ")
    
    if confirmacion.upper() == 'S':
        if funcion_nueva == 1 and vendidas_funcion1 < stock_funcion1:
            vendidas_funcion2 -= 1
            vendidas_funcion1 += 1
            compradores[nombre] = 1
            print(f"Cambio exitoso. Ahora está en función 1.")
        elif funcion_nueva == 2 and vendidas_funcion2 < stock_funcion2:

            vendidas_funcion1 -= 1
            vendidas_funcion2 += 1
            compradores[nombre] = 2
            print(f"Cambio exitoso. Ahora está en función 2.")
        else:
            print(f"Error: no hay entradas disponibles para la función {funcion_nueva}.")
    else:
        print("Cambio cancelado.")


def mostrar_stock():
    """Muestra el stock disponible y vendido de cada función"""
    global stock_funcion1, stock_funcion2, vendidas_funcion1, vendidas_funcion2
    
    print("\n-- Stock de Funciones --")
    print(f"Función 1 (Viernes): Disponibles {stock_funcion1 - vendidas_funcion1}, Vendidas {vendidas_funcion1}")
    print(f"Función 2 (Sábado): Disponibles {stock_funcion2 - vendidas_funcion2}, Vendidas {vendidas_funcion2}")


def generar_reporte_completo():
    """Genera un reporte completo de todas las ventas"""
    global compradores, vendidas_funcion1, vendidas_funcion2
    
    print("\n-- REPORTE COMPLETO DE VENTAS --")
    print(f"Total de entradas vendidas: {len(compradores)}")
    print(f"Función 1 (Viernes): {vendidas_funcion1} vendidas")
    print(f"Función 2 (Sábado): {vendidas_funcion2} vendidas")
    
    if compradores:
        print("\nLista de compradores:")
        for nombre, funcion in sorted(compradores.items()):
            dia = "Viernes" if funcion == 1 else "Sábado"
            print(f"  - {nombre}: Función {funcion} ({dia})")
    else:
        print("\nNo hay compradores registrados.")


def main():
    """Función principal que ejecuta el programa"""
    while True:
        try:
            mostrar_menu()
            
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == '1':
                comprar_entrada()
            elif opcion == '2':
                cambio_funcion()
            elif opcion == '3':
                mostrar_stock()
            elif opcion == '4':
                print("Programa terminado...")
                break
            elif opcion == '5':
                # Opción oculta para administradores
                generar_reporte_completo()
            else:
                print("Debe ingresar una opción válida!!")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            print("Programa terminado...")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            print("Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()
