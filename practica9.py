menu = ([1, 'Agregar elementos'], [2, 'Listar'], [3, 'ordenar'], [4, 'Obtener la posición del elemento x'], [5, 'Obtener el número de ocurrencias del elemento x'], [6, 'Borrar elemento'], [7, 'Actualizar el valor de un elemento'], [8, 'Salir'])
print('')
print(' MENÚ DE OPCIONES:')
for x in menu:
    print(x[0], '--->', x[1])
Nombres = []
while True:
    eleccion = int(input('Cuál es tu opción? '))
    if eleccion == 1:
        elemento = input('Nombre: ')
        Nombres.append(elemento)
    if eleccion == 2:
        print('')
        print(' Esta es la lista:')
        print('')
        for i in sorted(Nombres):
            print(i)
    if eleccion == 3:
        print('')
        print(' Esta es la lista ordenada:')
        print('')
        Nombres.sort()
        for i in sorted(Nombres):
            print(i)
    if eleccion == 4:
        buscar = input('Buscar: ')
        print(Nombres.index(buscar))
    if eleccion == 5:
        repeticiones = input('Repeticiones de: ')
        print(Nombres.count(repeticiones))
    if eleccion == 6:
        eliminar = input('Eliminar: ')
        Nombres.remove(eliminar)
        print(Nombres)
    if eleccion == 7:
        print('')
        viejo = input('Nombre a actualizar: ')
        nuevo = input('Nuevo nombre: ')
        k = Nombres.index(viejo)
        Nombres.remove(viejo)
        Nombres.insert(k, nuevo)
        print(Nombres)
    if eleccion == 8:
        break
    if eleccion >8: 
        print('Ingresa una opción válida')
    if eleccion <1:
        print('Ingresa una opción válida')

