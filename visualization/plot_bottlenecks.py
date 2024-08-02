import matplotlib.pyplot as plt
import numpy as np

def generate_plot(cuellos_antes, cuellos_despues):
    num_access_points = len(cuellos_antes)
    frecuencias_antes = [len(cuellos_antes[i]) for i in range(num_access_points)]
    frecuencias_despues = [len(cuellos_despues[i]) for i in range(num_access_points)]

    # Configuración del gráfico
    x = np.arange(num_access_points)
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, frecuencias_antes, width, label='Antes de la optimización', color='blue')
    rects2 = ax.bar(x + width/2, frecuencias_despues, width, label='Después de la optimización', color='orange')

    ax.set_xlabel('Puntos de Acceso')
    ax.set_ylabel('Frecuencia de Cuellos de Botella')
    ax.set_title('Identificación de Cuellos de Botella por Punto de Acceso')
    ax.set_xticks(x)
    ax.set_xticklabels([f'PA {i+1}' for i in range(num_access_points)])
    ax.legend()

    # Etiquetas para cada barra
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.savefig('data/results/bottlenecks.png')
    plt.show()
