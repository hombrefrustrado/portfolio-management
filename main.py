#externo
import numpy as np
import matplotlib.pyplot as plt
import json
import os
from pathlib import Path

#propio
from Fondo import Fondo
from Cartera import Cartera

def dinero(cartera, tiempo):
    formula_interes_compuesto = lambda aportacion, interes, anyos: aportacion * (1 + interes / 100 ) ** anyos / (interes / 100)
    monto = 0
    for fondo in cartera.fondos:
        monto += formula_interes_compuesto(fondo.monto, fondo.rentabilidad, tiempo)
    return monto

def graficar_continuo_por_fondo(cartera, tiempo=40, pasos=1000):
    t = np.linspace(0, tiempo, pasos)
    
    # Patrimonio total
    total = np.zeros_like(t)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Colores automáticos
    colores = plt.cm.tab10.colors  # 10 colores distintos
    aporte_total = sum(fondo.monto for fondo in cartera.fondos)
    ahorro_total = aporte_total * t

    for i, fondo in enumerate(cartera.fondos):
        patrimonio_fondo = fondo.monto * ((1 + fondo.rentabilidad / 100) ** t - 1) / (fondo.rentabilidad / 100)
        total += patrimonio_fondo
        ax.plot(t, patrimonio_fondo, color=colores[i % len(colores)], linewidth=1.5, label=fondo.nombre)
    
    # Curva total
    ax.plot(t, total, color='black', linewidth=2, linestyle='--', label='Total')
    ax.plot(t, ahorro_total, color='gray', linewidth=1, linestyle=':', label='Ahorro Total')
    
    # Configuración gráfica
    ax.set_title("Evolución prevista del patrimonio por fondo")
    ax.set_xlabel("Años")
    ax.set_ylabel("Monto acumulado")
    ax.grid(True)
    ax.legend(loc='upper left')  # Muestra la leyenda
    
    plt.show()
def guardar_cartera(cartera,folder=None, file_name="configuracion.json"):

    if folder:
        os.makedirs(folder,exist_ok=True)
        path = os.path.join(folder,file_name)
    else:
        path = file_name
    with open(path,mode='w') as f:
        json.dump(cartera.to_dict(),f)
def cargar_cartera(folder=None, file_name="configuracion.json"):
    
    if folder:
        path = Path(folder) / file_name
    else:
        path = Path(file_name)

    with open(path, "r") as f:
        data = json.load(f)

    return Cartera.from_dict(data)

if __name__ == "__main__":
    cartera = Cartera()

    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡾⠧⠀⠀⠥⢀⡀⠀⠀
⠀⠀⠀⢀⣴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠑⡄
⠀⠀⢠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁
⠀⢀⣻⠁⠀⠀⠀⣰⢿⠀⠸⣽⣗⠖⠃⠀
⠀⠸⢼⠀⠀⠀⠀⣗⢽⠀⠄⠀⠁⠀⠀⠀
⠀⢸⠝⡆⠀⠀⠀⠈⠛⠃⠰⠤⢀⠀⠀⠀
⠀⠀⢯⠜⠦⡀⠀⠀⠀⠀⠀⠀⠀⠉⢂⠀
⠀⠀⠀⠓⢎⣝⠕⣲⡆⠀⡀⠀⠀⠀⠀⠆
⠀⠀⠀⠀⣄⠈⢙⢕⡇⠀⣿⡆⠀⠀⠀⢸
⠀⣠⠔⠉⠈⠑⠴⢬⡇⠀⡷⠃⠀⠀⠀⡈
⠸⡡⢓⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁
⠀⠈⠫⣎⡝⡢⢤⣀⠀⠀⣀⣀⡤⡾⠃⠀
⠀⠀⠀⠀⠉⠚⣔⣿⣤⣤⡽⠓⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠛⠛⠋⠀⠀⠀⠀⠀⠀
Aun no estan disponibles la opcion 4 y 5.
""")
    while(True):
        opcion = int(
            input(
                """
Selecciona una opcion
0 - Salir
1 - ver el resumen de tu cartera
2 - modificar fondos
3 - ver un gráfico de la evolución prevista del patrimonio
4 - Guardar configuracion
5 - Cargar configuracion
"""
            )
        )
        match(opcion):
            case 0:
                break
            case 1:
                print(cartera)
            case 2:
                cartera.modificar()
            case 3:
                anyos = int(input("Introduce el número de años para la proyección: "))
                graficar_continuo_por_fondo(cartera, tiempo=anyos)
            case 4:
                guardar_cartera(cartera)
            case 5:
                cartera = cargar_cartera()
            case _:
                print("opcion no valida")