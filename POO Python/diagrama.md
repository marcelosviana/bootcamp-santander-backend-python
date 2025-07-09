# Diagrama de Classes - Sistema Bancário

```mermaid
classDiagram
    class Cliente {
        - endereco: str
        - contas: list
        + realizar_transacao(conta: Conta, transacao: Transacao)
        + adicionar_conta(conta: Conta)
    }

    class PessoaFisica {
        - cpf: str
        - nome: str
        - data_nascimento: date
    }

    class Conta {
        - saldo: float
        - numero: int
        - agencia: str
        - cliente: Cliente
        - historico: Historico
        + saldo(): float
        + nova_conta(cliente: Cliente, numero: int): Conta
        + sacar(valor: float): bool
        + depositar(valor: float): bool
    }

    class ContaCorrente {
        - limite: float
        - limite_saques: int
    }

    class Historico {
        + adicionar_transacao(transacao: Transacao)
    }

    class Transacao {
        <<interface>>
        + registrar(conta: Conta)
    }

    class Deposito {
        - valor: float
    }

    class Saque {
        - valor: float
    }

    %% Heranças
    PessoaFisica --|> Cliente
    ContaCorrente --|> Conta
    Deposito --|> Transacao
    Saque --|> Transacao

    %% Relacionamentos
    Cliente "1" --> "*" Conta : "contas"
    Conta "1" --> "1" Historico : "historico"
    Conta --> Cliente : "cliente"
    Historico --> "*" Transacao : "transacoes"
    Cliente --> "*" Transacao : "realiza"
