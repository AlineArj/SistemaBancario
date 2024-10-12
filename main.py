def Menu():
    
    menu = '''      — MENU —
    
    ( 1 ) Deposito
    ( 2 ) Saque
    ( 3 ) Extrato
    ( 0 ) SAIR
    '''
    print(menu)
        
    return int(input("Escolha uma opção: "))
    
def Deposito(saldo):
    sucesso = 1
    
    valor_deposito = float(input("Valor do Deposito: R$ "))
    
    if valor_deposito < 1:
        print("Valor invalido para deposito.\n")
        return 
    else:
        saldo += valor_deposito
        return sucesso, valor_deposito, saldo

def Saque(saldo):
    sucesso = 1
    falha = -1
    
    valor_saque = float(input("Digite o valor que deseja sacar: ")) * -1
    
    if valor_saque > 1:
        print("Valor invalido para deposito.\n")
        return 
    elif abs(valor_saque) > saldo:
        print("Valor do saldo insuficiente!\n")
        return falha, valor_saque, saldo
    else:
        if abs(valor_saque) > 500:
            print("Valor do saque acima do permitido!\n")
            return
        else:
            saldo += valor_saque
            return sucesso, valor_saque, saldo
            
def Extrato (hist_operacao, hist_valores, hist_saldos):
    pass
    
    
saldo_inicial = 0
operacao = [0]
valores = [0]
saldos = [saldo_inicial]

print(f"{'#' * 9} BANCO ALINE {'#' * 9}\n\n")

while True:
    opcao = Menu()
        
    if opcao == 1:
        apoio = Deposito(saldo_inicial)
        if apoio == None:
            continue
        else:
            operacao.append(apoio[0])
            valores.append(apoio[1])
            saldos.append(apoio[2])
            saldo_inicial = apoio[2]
            
    elif opcao == 2: 
        apoio = Saque(saldo_inicial)
        if apoio == None:
            continue
        else:
            operacao.append(apoio[0])
            valores.append(apoio[1])
            saldos.append(apoio[2])
            saldo_inicial = apoio[2]
        
    elif opcao == 3:
        continue
        
    elif opcao == 0:
        print(f"\nBanco Aline agradece a sua preferencia.")
        print(f"VOLTE SEMPRE!")
        break
    else:
        print(f"\nA opção selecionada é inválida, tente novamente!\n")
    