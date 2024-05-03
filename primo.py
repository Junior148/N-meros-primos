continuar = True
while continuar:
    tentar = True
    while tentar:
        try:
            numero = int(input("Informe um número: "))
        except:
            print("Por favor, digite apenas números.")
        else:
            tentar = False
            print("O número digitado foi: ", numero)
    divisor = 1
    quantidade = 0
    while divisor <= numero:
      if ((numero % divisor) == 0):
          quantidade = quantidade + 1
      divisor = divisor + 1
    if quantidade == 2:
           print(numero, "É primo!")
    else: 
           print(numero, "Não é primo!")
    resposta = input("Deseja continuar digitando números? [s/n]")
    if resposta == 'n':
        continuar = False
    elif resposta == 's':
        continuar = True
         