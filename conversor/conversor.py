def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos" + tipo_pesos + "tienes?: ")
    pesos = float(pesos)
    valor_dolar = valor_dolar
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares") 

menu = """
Bienvenido al converson de moneda 💰️

1 - Pesos uruguayos
2 - Pesos argentinos
3 - Pesos colombianos

Elige una opcion: """

opcion = input (menu)

if opcion == '1':
    conversor("uruguayos", 40)
elif opcion == '2':
    conversor("argentinos", 129)
elif opcion == '3':
    conversor("colombianos", 4000)
else:
    print ("ingresa una opcion correcta por favor ")

    
