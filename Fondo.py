"""
La información que contiene esta clase será:
    1- el identificador númerico
    2- el nombre del fondo
    3- la rentabilidad media de los ultimos 5 años
    4- el riesgo del mismo
"""
class Fondo():
    def __init__(self, codigo, monto):
        """
        arg:
            fondo: el identificador alfa númerico del mismo.
        """
        self.codigo = codigo
        self.monto = monto

        self.nombre = self.codigo
        self.datos()
    
    def datos(self):
        self.rentabilidad = 10 # prueba de mockup, esto no es una rentabilidad real y se debería resolver con una consulta html
        self.riesgo = 4

    def resume(self):
        print(f"{self.nombre} - {self.codigo} : {self.monto} : {self.rentabilidad} % - {self.riesgo}")

    def __str__(self):
        return f"{self.nombre} - {self.codigo} : {self.monto} : {self.rentabilidad} % - {self.riesgo}"