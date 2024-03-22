class invalid_age(Exception):
    def __init__(self):
        super().__init__("Edad Invalida --> La edad ingresada no es invalida")

class invalid_option(Exception):
    def __init__(self):
        super().__init__("Opcion Invalida --> La opcion seleccionada es inavalida")

class invalid_amount(Exception):
    def __init__(self):
        super().__init__("Monto Invalido --> El monto ingresado no es valido")

class invalid_interest(Exception):
    def __init__(self):
        super().__init__("Interes Invalida -->El interes ingresado no es valido")

class hight_interest(Exception):
    def __init__(self):
        super().__init__("Interes alto --> El interes ingresado sube al 10% anual")

class low_amount_property(Exception):
    def __init__(self):
        super().__init__("Precio bajo --> El precio de la vivienda es muy bajo")

class invalid_quotas(Exception):
    def __init__(self):
        super().__init__("Cuota Invalida --> La cuota ingresada no es valida")

class invalid_valor(Exception):
    def __init__(self):
        super().__init__("Valor Invalido --> Debe ingresar valores positivos")