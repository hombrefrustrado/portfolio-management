from Fondo import Fondo
class Cartera():
    def __init__(self):  
        self.fondos = []
    
    def anyadir_fondo(self,codigo, monto=0):
        self.fondos.append(Fondo(codigo,monto))

    def __str__(self):
        if len(self.fondos) > 0:
            lineas = ["Nombre - Codigo : Monto : Rentabilidad % - Riesgo"]
            lineas += [str(fondo) for fondo in self.fondos]  # usamos __str__ de Fondo
            return "\n".join(lineas)
        else:
            return "Usted no tiene ningun activo"
    
    def resume(self):
        if (len(self.fondos) == 0):
            print("Usted no tiene ningun activo")
            return
        
        print("\n---------------------------\n Tu cartera tiene los siguientes activos")
        print("Nombre - Codigo : Monto : Rentabilidad % - Riesgo")
        
        
        for fondo in self.fondos:
            fondo.resume()
    def modificar(self):
        opcion = int(input("""
1- añadir fondo
2- eliminar fondo
3- editar fondo
"""))
        match(opcion):
            case 1:
                codigo = input("Introduce su código: ")
                monto = float(input("Introduce una aportacion anual: "))
                rentabilidad = float(input("Introduce la rentabilidad esperada: "))
                riesgo = float(input("Introduce el riesgo: "))
                self.fondos.append(Fondo(codigo,monto,rentabilidad,riesgo))
            case 2:
                codigo = input("Introduce su código: ")
                fondo = next((f for f in self.fondos if f.codigo == codigo), None)
                if fondo:
                    self.fondos.remove(fondo)
                else:
                    print("No se encontró ningún fondo con ese código.")
            case 3:
                codigo = input("Introduce su código: ")
                fondo = next((f for f in self.fondos if f.codigo == codigo), None)
                
                if not fondo:
                    print("No se encontró ningún fondo con ese código.")
                    return

                monto = float(input("Introduce una aportacion anual: "))
                interes = float(input("Introduce el interes previsto: "))
                riesgo = float(input("Introduce el riesgo: "))
                
                fondo.monto = monto
                fondo.riesgo = riesgo
                fondo.rentabilidad = interes
                print(f"Se actualizó el monto del fondo {codigo} a {monto}")
            