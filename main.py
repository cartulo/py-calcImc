# -*- coding: utf-8 -*-
try:
    inputPeso = float(input("Digite seu peso em Kg(Exemplo: 60): "))
    inputAltura = float(input("Digite sua altura em m(Exemplo: 1.70): "))

    calcularImc = inputPeso / (inputAltura * inputAltura)

except (TypeError, NameError, SyntaxError, ValueError):
    print("================================================")
    print("Erro nos caracteres digitados, utilize apenas números.")
    print("================================================")
    input("Pressione qualquer tecla para sair.")

except ZeroDivisionError:
    print("================================================")
    print("Impossível dividir por zero.")
    print("================================================")
    input("Pressione qualquer tecla para sair.")

match calcularImc:
    case calcularImc if calcularImc < 18.5:
        print("================================================")
        print("Seu IMC é: {0: .2f}.".format(calcularImc))
        print("Obesidade grau 0, classificação: Magreza.")
        print("================================================")
        input("Pressione qualquer tecla para sair.")

    case calcularImc if 18.5 < calcularImc < 24.9:
        print("================================================")
        print("Seu IMC é: {0: .2f}.".format(calcularImc))
        print("Obesidade grau 0, classificação: Normal.")
        print("================================================")
        input("Pressione qualquer tecla para sair.")

    case calcularImc if 25 < calcularImc < 29.9:
        print("================================================")
        print("Seu IMC é: {0: .2f}.".format(calcularImc))
        print("Obesidade grau 1, classificação: Sobrepeso.")
        print("================================================")
        input("Pressione qualquer tecla para sair.")

    case calcularImc if 30 < calcularImc < 39.9:
        print("================================================")
        print("Seu IMC é: {0: .2f}.".format(calcularImc))
        print("Obesidade grau 2, classificação: Obesidade.")
        print("================================================")
        input("Pressione qualquer tecla para sair.")

    case calcularImc if calcularImc > 40:
        print("================================================")
        print("Seu IMC é: {0: .2f}.".format(calcularImc))
        print("Obesidade grau 3, classificação: Obesidade Grave.")
        print("================================================")
        input("Pressione qualquer tecla para sair.")