menu = ([1, 'Agregar elementos'], [2, 'Listar'], [3, 'ordenar'], [4, 'Obtener la posición del elemento x'], [5, 'Obtener el número de ocurrencias del elemento x'], [6, 'Borrar elemento'], [7, 'Actualizar el valor de un elemento'], [8, 'Salir']menu = ([1, 'Agregar elementos'], [2, 'Listar'], [3, 'ordenar'], [4, 'Obtener la posición del elemento x'], [5, 'Obtener el número de ocurrencias del elemento x'], [6, 'Borrar elemento'], [7, 'Actualizar el valor de un elemento'], [8, 'Salir'])
print('')
print(' MENÚ DE OPCIONES:')
for x in menu:
    print(x[0], '--->', x[1])
Nombres = [] #declaramos una lista vacía
while True: 
    eleccion = int(input('Cuál es tu opción? '))
    if eleccion == 1:
        elemento = input('Nombre: ')
        Nombres.append(elemento) #Agregamos el nombre al final de la lista
    if eleccion == 2:
        print('')
        print(' Esta es la lista:')
        for i in Nombres: 
            print(i) #imprimimos los elementos y se mostrarán en forma listada
        print('')
    if eleccion == 3:
        print('')
        print(' Esta es la lista ordenada:')
        for i in sorted(Nombres): #La funcion sorted ordena la lista ya modificada a manera de lista 
            print(i) #imprimimos los elementos y se mostrarán en forma listada
    if eleccion == 4:
        buscar = input('Buscar: ')
        print('Posición: 'Nombres.index(buscar)) #Esta opcion únicamente imprime el primer indice que ocupa el nombre en la lista  
    if eleccion == 5:
        repeticiones = input('Apariciones de: ') #Le pedimos al usuario el nombre que quiera saber cuantas veces se repite
        print(Nombres.count(repeticiones)) #Con esta funcion contamos las repeticiones e imprimimos el número de veces que se repite
    if eleccion == 6:
        eliminar = input('Eliminar: ') #Le pedimos al usuario el nombre a eliminar
        Nombres.remove(eliminar) #removemos/borramos el nombre de la lista
        print(Nombres)
    if eleccion == 7:
        print('')
        viejo = input('Nombre a actualizar: ')  #Le pedimos al usuario el nombre que quiere reemplazar
        nuevo = input('Nuevo nombre: ') #Le pedimos el nuevo nombre
        k = Nombres.index(viejo)    #Le asignamos a k el número de indice del nombre a reemplazar
        Nombres.remove(viejo)   #Borramos el nombre
        Nombres.insert(k, nuevo) #Insertamos el nuevo nombre en la posición en donde estaba el nombre que borramos
        print(Nombres) #imprimimos la lista y corroboramos que ya no está el nombre inicial
    if eleccion == 8: #si seleccionamos el 8 simplemente salimos del ciclo y con eso el final de la ejecución
        break
    if eleccion >8: #Si el número ingresado es mayor a 8, le decimos al usuario que ingrese un número válido
        print('Ingresa una opción válida')
    if eleccion <1: #Si el número ingresado es menos a 1, le decimos al usuario que ingrese un número válido
        print('Ingresa una opción válida')
