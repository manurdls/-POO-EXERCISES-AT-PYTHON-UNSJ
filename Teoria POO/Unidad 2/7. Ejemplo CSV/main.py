import csv

if __name__ == '__main__':
    total = 0
    lineaCompleta = []
    archivo = open('compras.csv')
    reader = csv.reader(archivo, delimiter=';')
    for fila in reader:
        costo = float(fila[1]) * float(fila[2].replace(",","."))
        total += costo
        lineaCompleta = fila + [round(costo,2)] ##BUEN COMPLEMENTO A .append PARA NO ESCRIBIR 2 SENTENCIAS
        print(lineaCompleta)
    print('Total de compra: {0:.2f}'.format(total))
    archivo.close()