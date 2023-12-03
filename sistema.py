import heapq

def a_estrella(grafico, inicio, objetivo):
    lista_abierta = [(0, inicio)]
    vino_de = {}
    costo_g = {nodo: float('inf') for nodo in grafico}
    costo_g[inicio] = 0
    costo_f = {nodo: float('inf') for nodo in grafico}
    costo_f[inicio] = heuristica(inicio, objetivo)

    while lista_abierta:
        f_actual, nodo_actual = heapq.heappop(lista_abierta)

        if nodo_actual == objetivo:
            return reconstruir_camino(vino_de, nodo_actual)

        for vecino in grafico[nodo_actual]:
            costo_g_tentativo = costo_g[nodo_actual] + grafico[nodo_actual][vecino]
            
            if costo_g_tentativo < costo_g[vecino]:
                vino_de[vecino] = nodo_actual
                costo_g[vecino] = costo_g_tentativo
                costo_f[vecino] = costo_g_tentativo + heuristica(vecino, objetivo)
                heapq.heappush(lista_abierta, (costo_f[vecino], vecino))
    
    return None  # No se encontró un camino

def heuristica(nodo, objetivo):
    return 0

def reconstruir_camino(vino_de, nodo_actual):
    camino = [nodo_actual]
    while nodo_actual in vino_de:
        nodo_actual = vino_de[nodo_actual]
        camino.append(nodo_actual)
    return list(reversed(camino))

# Ejemplo de uso 1
grafico = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 2},
    'C': {'D': 1},
    'D': {'E': 3},
    'E': {}
}
# debe modificarse el grafo para poder verificar la mejor ruta en funcion del mismo
# Ejemplo de uso 2

# grafico = {
#     'A': {'B': 10, 'C': 30},
#     'B': {'A': 2},
#     'C': {'C': 1},
#     'D': {'E': 30},
#     'E': {'B': 35}
# }


inicio = 'A'
objetivo = 'E'

mejor_ruta = a_estrella(grafico, inicio, objetivo)
if mejor_ruta:
    print("La mejor ruta es:", mejor_ruta)
else:
    print("No se encontró una ruta válida.")
