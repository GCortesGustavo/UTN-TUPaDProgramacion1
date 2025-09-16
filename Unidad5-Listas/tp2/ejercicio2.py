# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
lista :list = []
for i in range(5):
    producto = input("Ingrese 5 productos: ").capitalize()
    lista.append(producto)

lista_ordenada = sorted(lista)

print('La lista ordenada es', lista_ordenada)

producto_eliminado:int = int(input('Deseas eliminar algun producto? 1:Si - 2:No '))

if producto_eliminado == 1:
    eliminado = input('Cual es el producto? ').capitalize()
    if eliminado in lista_ordenada:
        lista_ordenada.remove(eliminado)
else:
    print('El programa a finalizado')


print('La lista final es: ', lista_ordenada)