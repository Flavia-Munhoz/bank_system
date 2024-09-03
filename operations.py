# operations.py

# Variáveis globais para armazenar os dados
depositos = []
saques = []
saldo = 0.0
saque_diario_max = 3  # Número máximo de saques diários permitido
saque_diario = saque_diario_max # Inicialmente, o número de saques disponíveis é igual ao máximo
espaco = "_ _ _ _ _ _ __ _ _"

def depositar(valor):
    """Realiza um depósito na conta e atualiza o saldo."""
    global saldo
    if valor > 0:
        depositos.append(valor)
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

def sacar(valor):
    """Realiza um saque da conta, respeitando o limite diário e o valor máximo."""
    global saldo, saque_diario
    if saque_diario <= 0:
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
    if not depositos and not saques:
        print("\nNão foram realizadas movimentações.")
        return

    print("\n### Extrato ###\n")
    for deposito in depositos:
        print(f"Depósito:{espaco}R$ {deposito:.2f}")
    for saque in saques:
        print(f"\nSaque:{espaco}R$ {saque:.2f}")

    saques_realizados = saque_diario_max - saque_diario
    movimentacoes = len(depositos) + saques_realizados
    print(f"\nSaldo atual: R${espaco} {saldo:.2f}\n")
    print(f"Total de movimentações:{espaco} {movimentacoes}\n")
    print(f"Saque diário disponivel:{espaco} {saque_diario}\n")
