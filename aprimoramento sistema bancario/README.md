# 🏦 Sistema Bancário aprimorado em Python

Este é um sistema bancário simples desenvolvido em Python, que simula operações básicas como **depósito, saque, extrato, cadastro de clientes e criação de contas**.

## 🚀 Funcionalidades

- 📥 **Depósito**: Permite ao usuário depositar valores positivos na conta.
- 💸 **Saque**:
  - Limite diário de 3 saques.
  - Limite máximo de R$ 500,00 por saque.
  - Verificação de saldo antes da operação.
- 📄 **Extrato**: Exibe todas as movimentações e o saldo atual.
- 👤 **Cadastro de Cliente**:
  - Cadastro por CPF (único).
  - Armazena nome, data de nascimento e endereço completo.
- 🧾 **Criação de Conta**:
  - Cada cliente pode ter uma conta.
  - Agência padrão: `0001`.
  - Número da conta gerado automaticamente.

## 📋 Menu Principal

```
[d] Depositar
[s] Sacar
[e] Exibir extrato
[cl] Cadastrar cliente
[cc] Criar conta
[q] Sair
```

## 💻 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/) — linguagem principal
- Módulo `datetime` — controle de data para limitar os saques diários

## 🧠 Estrutura do Projeto

- `main()` — função principal que exibe o menu e controla o fluxo.
- `depositar()` — realiza depósitos.
- `sacar()` — realiza saques com validações.
- `exibir_extrato()` — mostra o histórico da conta.
- `cadastrar_clientes()` — adiciona novos clientes únicos por CPF.
- `criar_conta()` — vincula uma conta a um cliente existente.



## 🧑‍💻 Autor

Desenvolvido por **Marcelo Viana**  