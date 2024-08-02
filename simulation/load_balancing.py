import simpy
import random

# Parámetros de la simulación
NUM_ACCESS_POINTS = 5
NUM_DEVICES = 50
SIM_TIME = 100  # Tiempo total de la simulación en segundos

class PuntoDeAcceso:
    def __init__(self, env, id):
        self.env = env
        self.id = id
        self.carga = 0
        self.historial_carga = []

    def manejar_trafico(self, tasa_trafico):
        while True:
            # Simular la recepción de tráfico con fluctuaciones
            self.carga += tasa_trafico + random.uniform(-0.5, 0.5) * tasa_trafico
            self.historial_carga.append((self.env.now, self.carga))
            yield self.env.timeout(1)
            self.carga -= tasa_trafico

def dispositivo(env, puntos_de_acceso, tasa_trafico):
    while True:
        # Selección del punto de acceso usando el algoritmo Least Connections
        punto_acceso = min(puntos_de_acceso, key=lambda pa: pa.carga)
        yield env.timeout(random.expovariate(1))
        env.process(punto_acceso.manejar_trafico(tasa_trafico))
        yield env.timeout(random.uniform(10, 20))  # Periodo de inactividad aleatorio

def run_load_balancing_simulation():
    # Simulación antes de la optimización
    env = simpy.Environment()
    puntos_de_acceso = [PuntoDeAcceso(env, i) for i in range(NUM_ACCESS_POINTS)]

    # Tasas de tráfico más realistas (en Mbps)
    tasas_trafico_antes = [random.uniform(0.5, 2) for _ in range(NUM_DEVICES)]
    for tasa_trafico in tasas_trafico_antes:
        env.process(dispositivo(env, puntos_de_acceso, tasa_trafico))

    env.run(until=SIM_TIME)
    historial_antes = [pa.historial_carga.copy() for pa in puntos_de_acceso]

    # Simulación después de la optimización (Least Connections)
    env = simpy.Environment()
    puntos_de_acceso = [PuntoDeAcceso(env, i) for i in range(NUM_ACCESS_POINTS)]

    tasas_trafico_despues = [t * 0.8 for t in tasas_trafico_antes]  # Reducción del 20%
    for tasa_trafico in tasas_trafico_despues:
        env.process(dispositivo(env, puntos_de_acceso, tasa_trafico))

    env.run(until=SIM_TIME)
    historial_despues = [pa.historial_carga.copy() for pa in puntos_de_acceso]

    return historial_antes, historial_despues
