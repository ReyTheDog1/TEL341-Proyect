import matplotlib.pyplot as plt

def generate_plot(historial_antes, historial_despues):
    tiempo_antes, ancho_de_banda_antes = zip(*historial_antes)
    tiempo_despues, ancho_de_banda_despues = zip(*historial_despues)

    plt.figure(figsize=(10, 5))
    plt.plot(tiempo_antes, ancho_de_banda_antes, label='Antes de la optimización', linestyle='--', color='blue')
    plt.plot(tiempo_despues, ancho_de_banda_despues, label='Después de la optimización', linestyle='-', color='green')
    plt.title('Uso Total de Ancho de Banda')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Ancho de Banda Utilizado (Mbps)')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.savefig('data/results/bandwidth_usage_realistic.png')
    plt.show()
