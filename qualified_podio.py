def podio_olimpico(p1, p2, p3):
    # Implemente aqui a lógica da função
    if p1 < p2 < p3:
      return f"1 - {p1} minutos\n2 - {p2} minutos\n3 - {p3} minutos\n"
    elif p1 <= p3 <= p2:
      return (f'1 - {p1} minutos\n2 - {p3} minutos\n3 - {p2} minutos\n')
    elif p2 <= p1 <= p3:
      return (f'1 - {p2} minutos\n2 - {p1} minutos\n3 - {p3} minutos\n')
    elif p2 <= p3 <= p1:
      return (f'1 - {p2} minutos\n2 - {p3} minutos\n3 - {p1} minutos\n')
    elif p3 <= p1 <= p2:
      return (f'1 - {p3} minutos\n2 - {p1} minutos\n3 - {p2} minutos\n')
    elif p3 <= p2 <= p1:
      return (f'1 - {p3} minutos\n2 - {p2} minutos\n3 - {p1} minutos\n')
    return 

  
tempo_chegada1 = 120
tempo_chegada2 = 90
tempo_chegada3 = 110
print(podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3))
