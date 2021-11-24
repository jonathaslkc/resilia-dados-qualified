def podio_olimpico(tem1, tem2, tem3, cor1, cor2, cor3):
    # Implemente aqui a lógica da função
    if tem1 < tem2 < tem3:
      return f'1 - {cor1} - {tem1} minutos\n2 - {cor2} - {tem2} minutos\n3 - {cor3} - {tem3} minutos\n'
    elif tem1 < tem3 < tem2:
      return f'1 - {cor1} - {tem1} minutos\n2 - {cor3} - {tem3} minutos\n3 - {cor2} - {tem2} minutos\n'
    elif tem2 < tem1 < tem3:
      return f'1 - {cor2} - {tem2} minutos\n2 - {cor1} - {tem1} minutos\n3 - {cor3} - {tem3} minutos\n'
    elif tem2 < tem3 < tem1:
      return f'1 - {cor2} - {tem2} minutos\n2 - {cor3} - {tem3} minutos\n3 - {cor1} - {tem1} minutos\n'
    elif tem3 < tem1 < tem2:
      return f'1 - {cor3} - {tem3} minutos\n2 - {cor1} - {tem1} minutos\n3 - {cor2} - {tem2} minutos\n'
    elif tem3 < tem2 < tem1:
      return f'1 - {cor3} - {tem3} minutos\n2 - {cor2} - {tem2} minutos\n3 - {cor1} - {tem1} minutos\n'

  
tempo_chegada1 = 120
tempo_chegada2 = 90
tempo_chegada3 = 110
nome_corredor1 = "José"
nome_corredor2 = "Roberto"
nome_corredor3 = "André"
print(podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3))
