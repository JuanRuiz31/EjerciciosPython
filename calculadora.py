entradaSuma = 0;

while True:
    entrada = input("Intruduce una entrada: ")
    if entrada=="stop":
        break;
    else:
        entradaNumero = int(entrada)
        entradaSuma += entradaNumero
   

print(entradaSuma)