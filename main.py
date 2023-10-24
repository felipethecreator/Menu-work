# import matplotlib.pyplot as plt
# import numpy as np

class Funcionario:
    def __init__(self):
        nome = ""
        cargo = ""
        salario = 0
        horasTrabalhadas = 0

def gravarDados(funcionario, numero) :

    f = open('folha_pag.txt', 'a', encoding="utf-8")
    f.write(f"----------- Funcionario {numero} ---------\n")
    f.write("Nome: " + funcionario.nome + "\n")
    f.write("Cargo: " + funcionario.cargo + "\n")
    f.write("Salário: R$ " + str(funcionario.salario) + "\n")
    f.write("Horas Trabalhadas: " + str(funcionario.horasTrabalhadas) + "\n")
    f.write("\n")
    f.close()
    numero += 1


# funcionario1 = Funcionario()

# print('--------------------------------------------')
# print("Nome do funcionário: ", funcionario1.nome)
# print("Cargo equivalente: ", funcionario1.cargo)
# print("Salário do funcionário: ", funcionario1.salario)
# print("Horas trabalhadas do funcionário: ", funcionario1.horasTrabalhadas)
# print('--------------------------------------------')

def cadastroFuncionario(numero) :
    
    funcionario = Funcionario()

    funcionario.nome = input("Digete o nome: ")
    funcionario.cargo = input("Digete o cagu: ")
    salario = float(input("Digete o salaryo: "))
    funcionario.salario = calcularImposto(salario)
    funcionario.horasTrabalhadas = int(input("Digete as ooras: "))
    gravarDados(funcionario, numero)


def calcularImposto(salario):
        if salario <= 1500.00:
            return salario 
        elif salario <= 3000.00:
            return salario * 0.85
        elif salario <= 5000.00:
            return salario * 0.80
        else:
            return salario * 0.73


def menu() :
    numero = 1
    while True:
        print("-------------- MENU ---------------")
        print(" 1 - Cadastrar funcionário")
        print(" 2 - Calcular imposto de renda")
        print(" 99 - Fechar o programa")
        print("-----------------------------------")

        opcao = int(input("Digite alguma opção: "))
        if opcao == 1 :
            cadastroFuncionario(numero)
            numero += 1
        elif opcao == 2 :
            calcularImposto()
        elif opcao == 99 :
            break


menu()
    

    
    




