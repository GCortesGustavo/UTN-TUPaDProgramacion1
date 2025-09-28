precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Ejercicio 2:
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)
print('==========================')
#Ejercicio 3:
lista_frutas :list = []
lista_frutas.append(precios_frutas.keys())


print('La lista de los nombres de las frutas es: ', lista_frutas)