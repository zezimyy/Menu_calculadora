n1 = 0
n2 = 0
loop = True
resultado = 0

while loop == True:
    n1 = int(input("Digite um numero - "))
    n2 = int(input("Digite um numero - "))
    print()
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Alterar numero")
    print("[5] Sair")
    print()
    resultado = int(input("Oque deseja fazer? "))

    if resultado == 1:
        print("{}".format(n1 + n2))
        print()

    if resultado == 2:
        print("{}".format(n1 * n2))
        print()

    if resultado == 3:
      if n1 > n2:
        print("O maior numero é o {}".format(n1))
        print()
      else:
        print("O maior numero é {}".format(n2))
        print()
  
    if resultado == 5:
        loop = False

    while resultado == 4:
        n1 = int(input("Digite um numero - "))
        n2 = int(input("Digite um numero - "))
        print()
        print("[1] Somar")
        print("[2] Multiplicar")
        print("[3] Maior")
        print("[4] Alterar numero")
        print("[5] Sair")
        print()

        resultado = int(input("Oque deseja fazer? "))

        if resultado == 1:
            print("{}".format(n1 + n2))
            print()

        if resultado == 2:
            print("{}".format(n1 * n2))
            print()
        if resultado == 3:
          if n1 > n2:
            print("O maior numero é o {}".format(n1))
            print()
          else:
            print("O maior numero é {}".format(n2))
            print()
        if resultado == 5:
            loop = False
