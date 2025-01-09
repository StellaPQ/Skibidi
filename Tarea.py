lista_de_palabritas = {
    "LMFAO": "Algo extremadamente divertido",
    "LMAO": "Algo muy divertido",
    "LOL": "Algo gracioso",
    "AFK": "Away From Keyboard - Lejos del teclado / Inactivo",
    "XD": "Representa una cara riendo"
}


palabra = input("Escribe una palabra de las generaciones recientes y te la traduciremos en un lenguaje entendible!")

if palabra in lista_de_palabritas.keys():
    print(lista_de_palabritas[palabra])
else:
    print("No se ha encontrado esa palabra")
