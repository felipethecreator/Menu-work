import matplotlib.pyplot as plt
import os
import time

precos = {1: 10.0, 2: 15.0, 3: 20.0, 4: 25.0, 5: 30.0, 6: 35.0, 7: 40.0, 8: 45.0, 9: 50.0, 10: 55.0}

quantidades_vendidas = {}

def ler_dados():
    for i in range(1, 11):
        quantidade = int(input(f"Digite a quantidade vendida da mercadoria {i}: "))
        quantidades_vendidas[i] = quantidade

def calcular_faturamento():
    faturamento = 0.0
    for mercadoria, quantidade in quantidades_vendidas.items():
        faturamento += quantidade * precos[mercadoria]
    return faturamento

def imprimir_faturamento():
    faturamento = 0.0
    for mercadoria, quantidade in quantidades_vendidas.items():
        faturamento += quantidade * precos[mercadoria]
    print("Faturamento mensal do armazém:")
    for mercadoria, quantidade in quantidades_vendidas.items():
        print(f"Mercadoria {mercadoria}: Quantidade vendida = {quantidade}, Preço = {precos[mercadoria]}")
    print(f"Total Faturado: {faturamento}")

def calcular_percentuais():
    faturamento = calcular_faturamento()
    percentuais = {k: (v * precos[k] / faturamento) * 100 for k, v in quantidades_vendidas.items()}
    return percentuais

def imprimir_percentuais():
    percentuais = calcular_percentuais()
    print("Percentuais de vendas por mercadoria:")
    for mercadoria, percentual in percentuais.items():
        print(f"Mercadoria {mercadoria}: {percentual:.2f}% do faturamento")

def gravar_em_arquivo():
    with open("armazem/vendas.txt", "w") as arquivo:
        arquivo.write("Mercadoria,Quantidade Vendida,Preço\n")
        for mercadoria, quantidade in quantidades_vendidas.items():
            arquivo.write(f"{mercadoria},{quantidade},{precos[mercadoria]}\n")

def gerar_grafico():
    sorted_vendas = sorted(quantidades_vendidas.items(), key=lambda x: x[1], reverse=True)
    top5 = sorted_vendas[:5]
    mercadorias, quantidades = zip(*top5)
    plt.bar(mercadorias, quantidades)
    plt.xlabel("Mercadorias")
    plt.ylabel("Quantidade Vendida")
    plt.title("Top 5 Mercadorias Mais Vendidas")
    plt.show()
    
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

def menu():
    while True:
        print(
        """
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|                           MENU                          |
|---------------------------------------------------------|
|                                                         |
|  1 - Registrar quantidade de vendas                     |
|  2 - Imprimir faturamento                               |
|  3 - Imprimir percentuais de vendas                     |
|  4 - Gravar dados em arquivo                            |
|  5 - Gerar gráfico das cinco mercadorias mais vendidas  |
|  0 - Fechar o programa                                  |
|                                                         |
|_________________________________________________________|
        """
        )
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            os.system('clear')
            ler_dados()
            loading(3)
            os.system('clear')
            print("\nCadastrado com sucesso!")
            time.sleep(2)
            os.system('clear')
            
        elif opcao == 2:
            os.system('clear')
            loading(3)
            os.system('clear')
            imprimir_faturamento()
            time.sleep(8)
            os.system('clear')
            
        elif opcao == 3:
            os.system('clear')
            loading(3)
            os.system('clear')
            imprimir_percentuais()
            time.sleep(6)
            os.system('clear')
        
        elif opcao == 4:
            os.system('clear')
            gravar_em_arquivo()
            loading(3)
            os.system('clear')
        
        elif opcao == 5:
            os.system('clear')
            loading(3)
            os.system('clear')
            gerar_grafico()
            time.sleep(8)
            os.system('clear')
        
        elif opcao == 0:
            break
        
        else:
            print("Opção inválida. Tente novamente.")

menu()
