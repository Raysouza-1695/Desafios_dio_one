# Criando um Sistema Bancário com Python
menu_inicial = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """ # Menu de opções iniciais

menu = """" 

[4] Voltar ao menu inicial 
[0] Sair 

 => """  # Menu de opções após realizar uma operação

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu_inicial)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: ")) # Solicita o valor do depósito

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação realizada com sucesso!")
            opcao = input(menu) # Menu de opções após realizar uma operação

            
        else:
            print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro caso o valor informado seja inválido

    elif opcao == "2": 
        valor = float(input("Informe o valor do saque: ")) # Solicita o valor do saque
       

        excedeu_saldo = valor > saldo # Verifica se o valor do saque excede o saldo

        excedeu_limite = valor > limite # Verifica se o valor do saque excede o limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES # Verifica se o número de saques excede o limite
        

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
      

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
    

        elif valor > 0: # Verifica se o valor do saque é válido
            saldo -= valor # Atualiza o saldo
            extrato += f"Saque: R$ {valor:.2f}\n" # Adiciona a movimentação ao extrato
            numero_saques += 1
            print("Saque realizado com sucesso!")
            opcao = input(menu)

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3": # Exibe o extrato e o saldo
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        print("\n")
        print("Operação realizada com sucesso!")
        opcao = input(menu) # Menu de opções após realizar uma operação
        
    if opcao == "0":# Sair do programa
        print("Obrigado por utilizar o nosso sistema!")
        break
   

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
