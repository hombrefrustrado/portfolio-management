import json
"""
La información que contiene esta clase será:
    1- el identificador númerico
    2- el nombre del fondo
    3- la rentabilidad media de los ultimos 5 años
    4- el riesgo del mismo
"""
class Fondo():
    def __init__(self, codigo, monto, rentabilidad=10, riesgo=4):
        """
        arg:
            fondo: el identificador alfa númerico del mismo.
        """
        self.codigo = codigo
        self.rentabilidad = rentabilidad
        self.riesgo = riesgo
        self.monto = monto
        self.nombre = self.codigo
    
    def resume(self):
        print(f"{self.nombre} - {self.codigo} : {self.monto} : {self.rentabilidad} % - {self.riesgo}")

    def __str__(self):
        return f"{self.nombre} - {self.codigo} : {self.monto} : {self.rentabilidad} % - {self.riesgo}"
    def to_dict(self):
        return {
            "codigo":self.codigo,
            "nombre":self.nombre,
            "monto":self.monto,
            "rentabilidad":self.rentabilidad,
            "riesgo":self.riesgo
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            codigo=data["codigo"],
            monto=data["monto"],
            rentabilidad=data["rentabilidad"],
            riesgo=data["riesgo"]
        )
    