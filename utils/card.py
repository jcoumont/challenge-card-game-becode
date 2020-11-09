class Symbol:
    """ Class defining a card symbol characterized by :
        - color
        - symbol
    """

    # ©
    def __init__(self, color: str, icon: str):
        '''
        Constructon

        :param color: a string that represents the color (black or red)
        :param icon:  a string that represents the symbol (♥,♦,♣,♠)
        '''
        allowed_colors = ['black','red']
        allowed_symbols = ['♥','♦','♣','♠']
        if color not in allowed_colors:
            raise ValueError(color)
        self.color = color
        if icon not in allowed_symbols:
            raise ValueError(icon)
        self.icon = icon

    def __str__(self):
        return f"{self.color} {self.icon}"

class Card(Symbol):
    """ Class defining a playing card characterized
        - his force
        - his color
        - his symbol

        It inherits from the class Symbol
    """

    def __init__(self, value: str, color: str, icon: str):
        '''
        Constructor

        :param value : a string that represents the force of the card
        :param color: a string that represents the color (black or red)
        :param icon:  a string that represents the symbol (♥,♦,♣,♠)
        '''
        super().__init__(color, icon)
        
        allowed_values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        if value not in allowed_values:
            raise ValueError(value)
        self.value = value
        
    def __str__(self):
        return f"{self.value} {self.color} {self.icon}"
    
    def __repr__(self):
        return f"{self.value} {self.color} {self.icon}"

