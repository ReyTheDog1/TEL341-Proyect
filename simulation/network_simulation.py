import simpy
import random

# Parámetros de la simulación
NUM_DEVICES = 50
SIM_TIME = 100  # Tiempo total de la simulación en segundos
ANCHO_DE_BANDA_MAX = 1000  # Ancho de banda máximo disponible en Mbps

class Red:
    def __init__(self, env):
        self.env = env
        self.uso_ancho_de_banda = 0
        self.historial_ancho_de_banda = []

    def generar_trafico(self, tasa_trafico):
        while True:
            # Simular la generación de tráfico con fluctuaciones
            self.uso_ancho_de_banda += tasa_trafico + random.uniform(-0.5, 0.5) * tasa_trafico
            self.historial_ancho_de_banda.append((self.env.now, self.uso_ancho_de_banda))
            yield self.env.timeout(1)
            self.uso_ancho_de_banda -= tasa_trafico

def dispositivo(env, red, tasa_trafico):
    while True:
        # Periodos de actividad e inactividad
        yield env.timeout(random.expovariate(1))
        env.process(red.generar_trafico(tasa_trafico))
        yield env.timeout(random.uniform(10, 20))  # Periodo de inactividad aleatorio

# Función principal para ejecutar la simulación
def run_simulation():
    # Simulación antes de la optimización
    env = simpy.Environment()
    red = Red(env)

    # Tasas de tráfico más realistas (en Mbps)
    tasas_trafico_antes = [random.uniform(0.5, 2) for _ in range(NUM_DEVICES)]
    for tasa_trafico in tasas_trafico_antes:
        env.process(dispositivo(env, red, tasa_trafico))

    env.run(until=SIM_TIME)
    historial_antes = red.historial_ancho_de_banda.copy()

    # Simulación después de la optimización
    env = simpy.Environment()
    red = Red(env)

    # Reducción de la tasa de tráfico después de la optimización
    tasas_trafico_despues = [t * 0.8 for t in tasas_trafico_antes]  # Reducción del 20%
    for tasa_trafico in tasas_trafico_despues:
        env.process(dispositivo(env, red, tasa_trafico))

    env.run(until=SIM_TIME)
    historial_despues = red.historial_ancho_de_banda

    return historial_antes, historial_despues
