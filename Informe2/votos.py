VotosValidos = int(input("Ingrese votos validos: "))
VotosPartido = int(input("Ingrese votos por su partido: "))

umbral = VotosValidos * 0.03

if VotosPartido > umbral:
    print("Su partido tendra curules")
else:
    print("Se quemaron")