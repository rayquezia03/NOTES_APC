usuario_x = float(input("Digite a coordenada x da localização do usuário: "))
usuario_y = float(input("Digite a coordenada y da localização do usuário: "))

taxisx = [10, 20, 30, 40]  # Exemplo de coordenadas x dos táxis
taxisy = [5, 15, 25, 35]   # Exemplo de coordenadas y dos táxis

distancias = []

for i in range(len(taxisx)):
    distancia = ((taxisx[i] - usuario_x) ** 2 + (taxisy[i] - usuario_y) ** 2) ** 0.5
    distancias.append(distancia)

indice_taxi_mais_proximo = 0
menor_distancia = distancias[0]

for i in range(1, len(distancias)):
    if distancias[i] < menor_distancia:
        menor_distancia = distancias[i]
        indice_taxi_mais_proximo = i

taxi_mais_proximo_x = taxisx[indice_taxi_mais_proximo]
taxi_mais_proximo_y = taxisy[indice_taxi_mais_proximo]

print(f"O táxi mais próximo está na coordenada ({taxi_mais_proximo_x}, {taxi_mais_proximo_y}).")