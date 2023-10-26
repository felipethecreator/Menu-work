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
        desconto = 0.00
        salarioBruto = 0.00
        salarioLiquido = 0.00
        horasTrabalhadas = 0

def gravarDados(funcionario) :

    f = open('folha_pag.txt', 'a', encoding="utf-8")
    f.write("Nome: " + funcionario.nome + "\n")
    f.write("Cargo: " + funcionario.cargo + "\n")
    f.write("Salário Bruto: R$ " + "{:.2f}".format(funcionario.salarioBruto) + "\n")
    f.write("Salário Liquido: R$ " + "{:.2f}".format(funcionario.salarioLiquido) + "\n")
    f.write("Horas Trabalhadas: " + str(funcionario.horasTrabalhadas) + "\n")
    f.write("------------------------")
    f.write("\n")
    f.close()


def imprimirDados():
    
    global totalDescontos
    global totalSalarioBruto
    global totalSalarioLiquido

    print('\n--------------------------------------------')
    print("Total de descontos: R$ " + "{:.2f}".format(totalDescontos))
    print("Total de salário bruto: R$ " + "{:.2f}".format(totalSalarioBruto))
    print("Total de salário líquido: R$ " + "{:.2f}".format(totalSalarioLiquido))
    print('--------------------------------------------\n')

def cadastroFuncionario() :
    
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
    funcionario.horasTrabalhadas = int(input("Digite as horas de trabalho: "))
    gravarDados(funcionario)
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
            return 0.00
    elif salario <= 3000.00:
        resultado = salario * 0.15
        resultadoFormatado = float("{:.2f}".format(resultado))
        return resultadoFormatado
    elif salario <= 5000.00:
        resultado = salario * 0.20
        resultadoFormatado = float("{:.2f}".format(resultado))
        return resultadoFormatado
    else:
        resultado = salario * 0.27
        resultadoFormatado = float("{:.2f}".format(resultado))
        return resultadoFormatado
    
def loading(tempo) :
    value = 0
    while value <= tempo :
        print("")
        time.sleep(0.08)
        os.system('clear')
        print("/")
        time.sleep(0.08)
        os.system('clear')
        print("--")
        time.sleep(0.08)
        os.system('clear')
        print("\x5c")
        time.sleep(0.08)
        os.system('clear')
        value += 1
        
def lerArquivo() :
    with open("folha_pag.txt", "r", encoding="utf-8") as arquivo :
        texto = arquivo.readlines()
        
    for frase in texto:
        if "Nome" or "Cargo" or "Salário Bruto" or "Salário Liquido" or "Horas Trabalhadas" or "-" in frase:
            print(frase)


def menu() :
    os.system('clear')
    if os.stat('folha_pag.txt').st_size != 0 :
        decisao = input('Deseja continuar no arquivo já existente (s/n)? ')
        
        if decisao == 'n' or decisao == 'N':
            os.system('clear')
            decisao2 = input('O arquivo atual será apagado para iniciar outro, tem certeza (s/n)? ')
            
            if decisao2 == 's' or decisao == 'S':
                os.system('clear')
                f = open('folha_pag.txt', 'w', encoding='utf-8')
                f.truncate()
                
                os.system('clear')
            else:
                os.system('clear')
        else:
            os.system('clear')
    else:
        os.system('clear')
    
    while True:
        print(
        """
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|                    MENU                     |
|---------------------------------------------|
|                                             |
|  1 - Cadastrar funcionário                  |
|  2 - Visualizar dados gerais                |
|  3 - Visualizar relatório dos funcionários  |
|  0 - Fechar o programa                      |
|                                             |
|_____________________________________________|
        """
        )

        opcao = int(input("Digite alguma opção: "))
        
        if opcao == 1 :
            os.system('clear')
            
            cadastroFuncionario()
            loading(3)
            os.system('clear')
            print("\nCadastrado com sucesso!")
            time.sleep(2)
            os.system('clear')
                   
        elif opcao == 2 :
            os.system('clear')
            loading(2)
            
            if os.stat('folha_pag.txt').st_size == 0 :
                print('O arquivo está vazio, cadastre algum funcionário!')
                time.sleep(3)
                os.system('clear')
            else :  
                imprimirDados()
                time.sleep(6)
                os.system('clear')
                
        elif opcao == 3 :
            os.system('clear')
            loading(2)
            
            if os.stat('folha_pag.txt').st_size == 0 :
                print('O arquivo está vazio, cadastre algum funcionário!')
                time.sleep(3)
                os.system('clear')
            else :  
                lerArquivo()
                time.sleep(6)
                os.system('clear')
        elif opcao == 0 :
            break


menu()
    

    
    




