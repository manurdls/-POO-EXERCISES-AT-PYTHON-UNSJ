from claseTibetanSpaniel import TibetanSpaniel

if __name__ == '__main__':
    TibetanSpaniel.verRAza()
    miSpaniel = TibetanSpaniel('Jhon', 'hueso', 7)
    otroSpaniel = TibetanSpaniel('Coco', 'minion', 8)
    print(miSpaniel)
    print('Cambio de una variable de clase')
    TibetanSpaniel.obediencia = 9
    print(miSpaniel)
    print(otroSpaniel)