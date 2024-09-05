from datetime import date, datetime, timedelta, timezone
# Variáveis globais 
depositos = []
saques = []
saldo = 0.0
saque_diario_max = 10  # Número máximo de saques diários permitido
saque_diario = saque_diario_max # Inicialmente, o número de saque é igual ao máximo
espaco = " ___________ "
ultima_data_saque = datetime.now().date()# Inicializa com a data atual


def depositar(valor):
    """Realiza um depósito na conta e atualiza o saldo."""
    global saldo
    if valor > 0:
        depositos.append(valor)
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

def sacar(valor):# saque da conta, respeitando o limite diário, data e o valor máximo
    global saldo, saque_diario, ultima_data_saque
    data_atual = datetime.now().date()

    if data_atual != ultima_data_saque:
        saque_diario = saque_diario_max
        ultima_data_saque = data_atual

    if saque_diario <= 0 :
        print("Saque diário excedido.")
        return
    if valor > 500.00:
        print("Valor máximo por saque é R$ 500.00.")
        return
    if saldo < valor:
        print("Saldo insuficiente para saque.")
        return
    if valor > 0:
        saques.append(valor)
        saldo -= valor
        saque_diario -= 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para saque.")

def extrato():
    #Exibe o extrato da conta, incluindo o número de saques realizados e o total de depósitos
    data_atual = datetime.now().strftime("%d / %m / %y  %H : %M")
    if not depositos and not saques:
        print("\nNão foram realizadas movimentações.")
        return

    print("\n### Extrato ###\n")
    print(f"\nSaldo:{espaco}R${saldo:.2f}{espaco}{data_atual}\n")
    for deposito in depositos:
        print(f"Depósito:{espaco}R$ {deposito:.2f} #{data_atual}")
    for saque in saques:
        print(f"\nSaque:{espaco}R$ {saque:.2f} #{data_atual}")

    saques_realizados = saque_diario_max - saque_diario
    movimentacoes = len(depositos) + saques_realizados
    print(f"Total de movimentações:{espaco} {movimentacoes}\n")
    print(f"Saque diário disponivel:{espaco} {saque_diario}\n")



