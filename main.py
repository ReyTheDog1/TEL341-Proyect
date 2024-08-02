from simulation import network_simulation, load_balancing,bottleneck_analysis
from visualization import plot_bandwidth_usage, plot_load_distribution,plot_bottlenecks

def main():
    # Ejecutar simulaciones
    #historial_antes, historial_despues = network_simulation.run_simulation()

    # Generar gráficos
    #plot_bandwidth_usage.generate_plot(historial_antes, historial_despues)


    # Ejecutar simulaciones de balanceo de carga
    #historial_antes_load, historial_despues_load = load_balancing.run_load_balancing_simulation()
    # Generar gráfico de distribución de carga
    #plot_load_distribution.generate_plot(historial_antes_load, historial_despues_load)


    # Ejecutar simulaciones de cuellos de botella
    cuellos_antes, cuellos_despues = bottleneck_analysis.run_bottleneck_simulation()
    plot_bottlenecks.generate_plot(cuellos_antes, cuellos_despues)

if __name__ == "__main__":
    main()