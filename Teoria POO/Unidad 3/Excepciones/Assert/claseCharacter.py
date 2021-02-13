class Character(object):
    __character : str
    __bold : bool
    __italic : bool
    __underline : bool

    def __init__(self, character, bold = False, italic = False, underline = False):
        assert len(character) == 1, 'Se esperaba un solo caracter' #la asercion tiene que ser cierta para que no de error
        self.__character = character
        self.__bold = bold
        self.__italic = italic
        self.__underline = underline

    def __str__(self):
        bold = '*' if self.__bold else ''
        italic = '/' if self.__italic else ''
        underline = '_' if self.__underline else ''
        return bold + italic + underline + self.__character