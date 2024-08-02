import matplotlib.pyplot as plt
import numpy as np

def generate_plot(historial_antes, historial_despues):
    num_access_points = len(historial_antes)
    cargas_antes = [list(zip(*historial))[1] for historial in historial_antes]
    cargas_despues = [list(zip(*historial))[1] for historial in historial_despues]

    # Calcular la carga promedio para cada punto de acceso
    promedio_antes = [np.mean(carga) for carga in cargas_antes]
    promedio_despues = [np.mean(carga) for carga in cargas_despues]

    # Determinar el valor máximo para establecer el límite superior del eje Y
    valor_maximo = max(max(promedio_antes), max(promedio_despues))
    limite_superior = valor_maximo + 20  # Agregar espacio adicional

    # Configuración del gráfico
    x = np.arange(num_access_points)
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, promedio_antes, width, label='Antes de la optimización', color='blue')
    rects2 = ax.bar(x + width/2, promedio_despues, width, label='Después de la optimización', color='orange')

    ax.set_xlabel('Puntos de Acceso')
    ax.set_ylabel('Carga Promedio (Mbps)')
    ax.set_title('Distribución de Carga por Punto de Acceso')
    ax.set_xticks(x)
    ax.set_xticklabels([f'PA {i+1}' for i in range(num_access_points)])
    ax.set_ylim(0, limite_superior)  # Establecer límites del eje Y
    ax.legend()
    # Etiquetas para cada barra
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.savefig('data/results/load_distribution.png')
    plt.show()
