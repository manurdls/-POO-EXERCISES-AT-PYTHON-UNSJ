## Ejercicio 2
### Listas
En una aerolínea se quiere implementar para sus viajeros una promoción para
acumular puntos de los viajes que realizan.

Para ello, se necesita un sistema que sea capaz de gestionar el registro de
viajeros y las millas. Defina una clase viajeroFrecuente con los siguientes
atributos: número de viajero, DNI, nombre, apellido y las millas acumuladas.

Para esta clase implemente los siguientes metodos:

a-El constructor.

b-"cantidadTotaldeMillas", retorna la cantidad de millas acumuladas

c-"acumularMillas", recibe como parámetro la cantidad de millas recorridas
en el último viaje.

d-"canjearMillas", recibe como parámetro la cantidad de millas a canjear. Para
canjear las millas debe verificarse que la cantidad que sea necesita sea menor
o igual a la cantidad de millas acumuladas, caso contrario mostrar un cartel de
error en la operación.

### Implemente un programa que:
1-Lea un archivo separado por comas 20 instancias de la clase ViajeroFrecuente,
y las almacene en una lista.

2-Lea por teclado un número de viajero frecuente y presente un menú con las
siguientes opciones:

    a-Consultar cantidad de millas
    b-Acumular millas
    c-Canjear millas
    
3-Represente el espacio de almacenamiento en memoria para la lista
cargada con 4 viajeros.