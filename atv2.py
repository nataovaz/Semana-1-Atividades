t_gasto = input()
velocidade_media = input()

t_gasto = int(t_gasto)
velocidade_media = int(velocidade_media)

litros_necessarios = float((t_gasto*velocidade_media)/12.0)

print("{:.3f}".format(litros_necessarios))