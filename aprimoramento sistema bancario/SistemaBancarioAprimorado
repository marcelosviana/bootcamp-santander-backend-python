from datetime import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Exibir extrato
[cl] Cadastrar cliente
[cc] Criar conta
[q] Sair

=> """

def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("  ERRO - 51 \nSaldo insuficiente.")

    elif excedeu_limite:
        print("  ERRO - 51 \nLimite insuficiente.")

    elif excedeu_saques:
        print("  ERRO - 65 \nNúmero máximo de saques diários excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
            
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_clientes(clientes):
    cpf = input("Informe o CPF (somente números): ")
    
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("\n@@@ Já existe cliente com esse CPF! @@@")
            return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("=== Cliente criado com sucesso! ===")

def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF (somente números): ")
    
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("\n=== Conta criada com sucesso! ===")
            return {
                "agencia": agencia,
                "numero_conta": numero_conta,
                "cliente": cliente
            }
    
    print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
    return None

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    data_ultimo_saque = None
    clientes = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "s":
            hoje = datetime.now().date()
            if data_ultimo_saque is None or data_ultimo_saque != hoje:
                numero_saques = 0
                data_ultimo_saque = hoje

            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "cl":
            cadastrar_clientes(clientes)

        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)
            if conta:
                contas.append(conta)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()   