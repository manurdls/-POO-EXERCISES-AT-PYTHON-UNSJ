from claseAplicacion import Aplicacion
import requests

def getPrecioDolarVenta():
    dolarVenta = None
    complete_url = 'https://www.dolarsi.com/api/api.php?type=dolar'
    r = requests.get(complete_url)
    json = r.json()
    for i in range(len(json)):
        if json[i]['casa']['nombre'] == 'Oficial':
            dolarVenta = json[i]['casa']['venta']
            dolarVenta = dolarVenta.replace(',', '.')
            dolarVenta = float(dolarVenta)
    return dolarVenta


if __name__ == '__main__':
    dolarVenta = getPrecioDolarVenta()
    app = Aplicacion(dolarVenta)
    app.mainloop()