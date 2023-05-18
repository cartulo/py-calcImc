# -*- coding: utf-8 -*-
try:
    peso = float(input("Digite seu peso em Kg(Exemplo: 60): "))
    altura = float(input("Digite sua altura em m(Exemplo: 1.70): "))

    imc = peso / (altura * altura)

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

if imc < 18.5:
    print("================================================")
    print("Seu IMC é: {0: .2f}.".format(imc))
    print("Obesidade grau 0, classificação: Magreza.")
    print("================================================")
    input("Pressione qualquer tecla para sair.")

if (imc > 18.5) and (imc < 24.9):
    print("================================================")
    print("Seu IMC é: {0: .2f}.".format(imc))
    print("Obesidade grau 0, classificação: Normal.")
    print("================================================")
    input("Pressione qualquer tecla para sair.")

if (imc > 25) and (imc < 29.9):
    print("================================================")
    print("Seu IMC é: {0: .2f}.".format(imc))
    print("Obesidade grau 1, classificação: Sobrepeso.")
    print("================================================")
    input("Pressione qualquer tecla para sair.")

if (imc > 30) and (imc < 39.9):
    print("================================================")
    print("Seu IMC é: {0: .2f}.".format(imc))
    print("Obesidade grau 2, classificação: Obesidade.")
    print("================================================")
    input("Pressione qualquer tecla para sair.")

if imc > 40:
    print("================================================")
    print("Seu IMC é: {0: .2f}.".format(imc))
    print("Obesidade grau 3, classificação: Obesidade Grave.")
    print("================================================")
    input("Pressione qualquer tecla para sair.")