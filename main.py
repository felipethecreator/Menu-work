# import matplotlib.pyplot as plt
# import numpy as np

import os
import time


totalDescontos = 0
totalSalarioBruto = 0
totalSalarioLiquido = 0

class Funcionario:
    def __init__(self):
        nome = ""
        cargo = ""
        desconto = 0
        salarioBruto = 0
        salarioLiquido = 0
        horasTrabalhadas = 0

def gravarDados(funcionario, numero) :

    f = open('folha_pag.txt', 'a', encoding="utf-8")
    f.write(f"----------- Funcionario {numero} ---------\n")
    f.write("Nome: " + funcionario.nome + "\n")
    f.write("Cargo: " + funcionario.cargo + "\n")
    f.write("Salário Bruto: R$ " + str(funcionario.salarioBruto) + "\n")
    f.write("Salário Liquido: R$ " + str(funcionario.salarioLiquido) + "\n")
    f.write("Horas Trabalhadas: " + str(funcionario.horasTrabalhadas) + "\n")
    f.write("\n")
    f.close()
    numero += 1


def imprimirDados():
    
    global totalDescontos
    global totalSalarioBruto
    global totalSalarioLiquido

    print('\n--------------------------------------------')
    print("Total de descontos: ", totalDescontos)
    print("Total de salário bruto: ", totalSalarioBruto)
    print("Total de salário líquido: ", totalSalarioLiquido)
    print('--------------------------------------------\n')

def cadastroFuncionario(numero) :
    
    funcionario = Funcionario()
    global totalDescontos
    global totalSalarioBruto
    global totalSalarioLiquido

    funcionario.nome = input("\nDigite o nome: ")
    funcionario.cargo = input("Digite o cargo: ")
    salario = float(input("Digite o salário: "))
    funcionario.salarioBruto = salario
    funcionario.desconto = calcularDesconto(salario)
    funcionario.salarioLiquido = calcularImposto(salario)
    funcionario.horasTrabalhadas = int(input("Digite as horas: "))
    gravarDados(funcionario, numero)
    totalDescontos += funcionario.desconto
    totalSalarioBruto += funcionario.salarioBruto
    totalSalarioLiquido += funcionario.salarioLiquido


def calcularImposto(salario):
    if salario <= 1500.00:
        return salario 
    elif salario <= 3000.00:
        return salario * 0.85
    elif salario <= 5000.00:
        return salario * 0.80
    else:
        return salario * 0.73
        
def calcularDesconto(salario):
    if salario <= 1500.00:
            return 0.0
    elif salario <= 3000.00:
        return salario * 0.15
    elif salario <= 5000.00:
        return salario * 0.20
    else:
        return salario * 0.27


def menu() :
    f = open('folha_pag.txt', 'w', encoding="utf-8")
    f.truncate()
    
    numero = 1
    while True:
        print("\n-------------- MENU ---------------")
        print(" 1 - Cadastrar funcionário")
        print(" 2 - Calcular imposto de renda")
        print(" 99 - Fechar o programa")
        print("-----------------------------------")

        opcao = int(input("Digite alguma opção: "))
        if opcao == 1 :
            os.system('clear')
            cadastroFuncionario(numero)
            numero += 1
            time.sleep(2)
            print("\nCadastrado com sucesso!")
            time.sleep(2)
            os.system('clear')
        elif opcao == 2 :
            os.system('clear')
            imprimirDados()
            time.sleep(6)
            os.system('clear')
        elif opcao == 99 :
            break


menu()
    

    
    




