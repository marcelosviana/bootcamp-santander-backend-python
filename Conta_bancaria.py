from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
data_ultimo_saque = None

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Informe um valor válido.")

    elif opcao == "s":
        # Verifica se é um novo dia e zera o contador
        hoje = datetime.now().date()
        if data_ultimo_saque is None or data_ultimo_saque != hoje:
            numero_saques = 0
            data_ultimo_saque = hoje

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('''  ERRO - 51 \nSaldo insuficiente.''')
        elif excedeu_limite:
            print('''  ERRO - 51 \nLimite insuficiente.''')
        elif excedeu_saques:
            print('''  ERRO - 65 \nNúmero máximo de saques diários excedido.''')
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Informe um valor válido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
