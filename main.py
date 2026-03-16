#externo
import numpy as np
import matplotlib.pyplot as plt

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
    for i, fondo in enumerate(cartera.fondos):
        patrimonio_fondo = fondo.monto * (1 + fondo.rentabilidad / 100) ** t / (fondo.rentabilidad / 100)
        total += patrimonio_fondo
        ax.plot(t, patrimonio_fondo, color=colores[i % len(colores)], linewidth=1.5, label=fondo.nombre)
    
    # Curva total
    ax.plot(t, total, color='black', linewidth=2, linestyle='--', label='Total')
    
    # Configuración gráfica
    ax.set_title("Evolución prevista del patrimonio por fondo")
    ax.set_xlabel("Años")
    ax.set_ylabel("Monto acumulado")
    ax.grid(True)
    ax.legend(loc='upper left')  # Muestra la leyenda
    
    plt.show()
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
                graficar_continuo_por_fondo(cartera)