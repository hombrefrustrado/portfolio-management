from Fondo import Fondo
import json
import questionary
class Cartera():
    def __init__(self,fondos=None):  
        self.fondos = fondos if fondos is not None else []
    
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
        accion = questionary.select(
            "Gestión de Fondos:",
            choices=[
                "Añadir fondo",
                "Eliminar fondo",
                "Editar fondo",
                "Atrás"
            ]
        ).ask()

        if accion == "Atrás":
            return

        if accion == "Añadir fondo":
            codigo = questionary.text("Introduce su código:").ask()
            monto = float(questionary.text("Aportación anual:", validate=lambda t: t.replace('.','',1).isdigit()).ask())
            rentabilidad = float(questionary.text("Rentabilidad esperada:", validate=lambda t: t.replace('.','',1).isdigit()).ask())
            riesgo = float(questionary.text("Riesgo:", validate=lambda t: t.replace('.','',1).isdigit()).ask())
            
            self.fondos.append(Fondo(codigo, monto, rentabilidad, riesgo))
            print(f"Fondo {codigo} añadido.")

        elif accion in ["Eliminar fondo", "Editar fondo"]:
            if not self.fondos:
                print("No hay fondos registrados.")
                return

            nombres_fondos = [f.codigo for f in self.fondos]
            codigo_sel = questionary.select(
                f"Selecciona el fondo para {accion.lower()}:",
                choices=nombres_fondos
            ).ask()

            fondo = next(f for f in self.fondos if f.codigo == codigo_sel)

            if accion == "Eliminar fondo":
                confirmar = questionary.confirm(f"¿Seguro que quieres borrar {codigo_sel}?").ask()
                if confirmar:
                    self.fondos.remove(fondo)
                    print(f"Fondo {codigo_sel} eliminado.")

            elif accion == "Editar fondo":
                monto = float(questionary.text("Nueva aportación anual:", default=str(fondo.monto)).ask())
                interes = float(questionary.text("Nuevo interés previsto:", default=str(fondo.rentabilidad)).ask())
                riesgo = float(questionary.text("Nuevo riesgo:", default=str(fondo.riesgo)).ask())
                
                fondo.monto = monto
                fondo.rentabilidad = interes
                fondo.riesgo = riesgo
                print(f"Fondo {codigo_sel} actualizado correctamente.")
    
    def to_dict(self):
        return [fondo.to_dict() for fondo in self.fondos]
    
    @classmethod
    def from_dict(cls, data):
        fondos = [Fondo.from_dict(f) for f in data]
        return cls(fondos)