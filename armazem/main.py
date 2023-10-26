mercadorias = [
    {"produto": "Maçã", "preco": 1.00, "quantidade": 10},
    {"produto": "Banana", "preco": 0.30, "quantidade": 20},
    {"produto": "Laranja", "preco": 0.80, "quantidade": 15},
    {"produto": "Uva", "preco": 2.00, "quantidade": 5},
    {"produto": "Morango", "preco": 8.00, "quantidade": 3},
    {"produto": "Abacaxi", "preco": 4.00, "quantidade": 2},
    {"produto": "Pera", "preco": 1.00, "quantidade": 7},
    {"produto": "Melancia", "preco": 20.00, "quantidade": 1},
    {"produto": "Mamão", "preco": 4.00, "quantidade": 4},
    {"produto": "Limão", "preco": 0.50, "quantidade": 12},
    {"produto": "Cenoura", "preco": 0.50, "quantidade": 8},
    {"produto": "Batata", "preco": 1.00, "quantidade": 10},
    {"produto": "Tomate", "preco": 1.50, "quantidade": 9},
    {"produto": "Cebola", "preco": 1.00, "quantidade": 8},
    {"produto": "Alho", "preco": 0.50, "quantidade": 20},
    {"produto": "Pimentão", "preco": 1.00, "quantidade": 6},
    {"produto": "Brócolis", "preco": 1.50, "quantidade": 5},
    {"produto": "Couve", "preco": 1.00, "quantidade": 4},
    {"produto": "Alface", "preco": 2.00, "quantidade": 7},
    {"produto": "Espinafre", "preco": 2.00, "quantidade": 5},
    {"produto": "Aipo", "preco": 2.00, "quantidade": 3},
    {"produto": "Pepino", "preco": 1.00, "quantidade": 8},
    {"produto": "Abobrinha", "preco": 1.50, "quantidade": 6},
    {"produto": "Milho", "preco": 1.00, "quantidade": 10},
    {"produto": "Ervilha", "preco": 2.00, "quantidade": 4},
    {"produto": "Feijão", "preco": 4.00, "quantidade": 2},
    {"produto": "Arroz", "preco": 2.00, "quantidade": 3},
    {"produto": "Massa", "preco": 2.00, "quantidade": 5},
    {"produto": "Pão", "preco": 5.00, "quantidade": 6},
    {"produto": "Leite", "preco": 2.00, "quantidade": 10},
    {"produto": "Queijo", "preco": 5.00, "quantidade": 3},
    {"produto": "Iogurte", "preco": 1.00, "quantidade": 5},
    {"produto": "Manteiga", "preco": 5.00, "quantidade": 4},
    {"produto": "Ovo", "preco": 1.00, "quantidade": 30},
    {"produto": "Frango", "preco": 8.00, "quantidade": 2},
    {"produto": "Carne bovina", "preco": 20.00, "quantidade": 3},
    {"produto": "Carne de porco", "preco": 10.00, "quantidade": 2},
    {"produto": "Peixe", "preco": 15.00, "quantidade": 4},
    {"produto": "Camarão", "preco": 40.00, "quantidade": 1},
    {"produto": "Lagosta", "preco": 60.00, "quantidade": 1},
    {"produto": "Salmão", "preco": 30.00, "quantidade": 2},
    {"produto": "Atum", "preco": 4.00, "quantidade": 3},
    {"produto": "Sardinha", "preco": 2.00, "quantidade": 5},
    {"produto": "Bacon", "preco": 8.00, "quantidade": 3},
    {"produto": "Linguiça", "preco": 5.00, "quantidade": 4},
    {"produto": "Presunto", "preco": 10.00, "quantidade": 2},
    {"produto": "Salsicha", "preco": 3.00, "quantidade": 5},
    {"produto": "Azeite de oliva", "preco": 10.00, "quantidade": 2},
    {"produto": "Óleo de cozinha", "preco": 5.00, "quantidade": 2},
    {"produto": "Vinagre", "preco": 2.00, "quantidade": 3},
    {"produto": "Sal", "preco": 2.00, "quantidade": 4},
    {"produto": "Açúcar", "preco": 2.00, "quantidade": 3},
    {"produto": "Farinha", "preco": 2.00, "quantidade": 5},
    {"produto": "Cereal matinal", "preco": 5.00, "quantidade": 2},
    {"produto": "Aveia", "preco": 2.00, "quantidade": 3},
    {"produto": "Mel", "preco": 15.00, "quantidade": 2},
    {"produto": "Ketchup", "preco": 3.00, "quantidade": 2},
    {"produto": "Mustarda", "preco": 2.00, "quantidade": 3},
    {"produto": "Maionese", "preco": 3.00, "quantidade": 3},
    {"produto": "Molho de soja", "preco": 3.00, "quantidade": 3},
]

def adicionarQuantidade(mercadorias):
    for i in range(len(mercadorias)):
        mercadorias[i]['quantidade'] = input("Quantidade de vendas de " + mercadorias[i]['produto'] + ": ")
        
    print(mercadorias[0]['quantidade'])
        

while True:
    print(
        """
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
|                    MENU                     |
|---------------------------------------------|
|                                             |
|   1 - Adicionar quantidade de um produto    |
|                                             |
|_____________________________________________|
        """
    )

    opcao = int(input("Digite alguma opção: "))
    
    if opcao == 1 :
        adicionarQuantidade(mercadorias)