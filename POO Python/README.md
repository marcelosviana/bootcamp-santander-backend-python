# 🏦 Sistema Bancário em Python - POO

Projeto de um sistema bancário simples, orientado a objetos, com suporte a múltiplas contas, saques com limite diário e histórico de transações.

![Badge Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Badge Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

---

## 🚀 Funcionalidades

- Cadastro de clientes (Pessoa Física)
- Criação de contas correntes com limite de saque diário
- Saques e depósitos com validação de saldo e limite
- Histórico completo de transações
- Contador de saques que reinicia a cada novo dia
- Design modular e reutilizável (POO com boas práticas)

---

## 📚 Tecnologias e Conceitos

- `Python 3.10+`
- Programação Orientada a Objetos (POO)
- Classes, herança, polimorfismo, abstração
- Interface com `ABC`
- `@property`, `@classmethod`, `@abstractmethod`
- Controle de fluxo com data/hora (`datetime`)
- Boas práticas segundo a `PEP8`

---

## 💡 Exemplo de uso

```python
from datetime import datetime
from banco import PessoaFisica, ContaCorrente, Deposito, Saque

cliente = PessoaFisica("Marcelo Viana", "1990-01-01", "12345678900", "Rua Python, 42")
conta = ContaCorrente(numero=1, cliente=cliente)

cliente.adicionar_conta(conta)

cliente.realizar_transacao(conta, Deposito(1000))
cliente.realizar_transacao(conta, Saque(300))
cliente.realizar_transacao(conta, Saque(150))

print(f"Saldo atual: R$ {conta.saldo:.2f}")
```





---

## 📌 Diferenciais

- 🔄 Reset automático de limite de saques por data
- 🔒 Design com encapsulamento e métodos protegidos
- 🧪 Pronto para ser expandido com testes ou interface

---

## 🤝 Contato

**Marcelo Viana**  
📧 marceloviana836@gmail.com  
🌐 [marceloviana.vercel.app](https://marceloviana.vercel.app)  
🐙 [github.com/marcelosviana](https://github.com/marcelosviana)

---

> *“A melhor forma de prever o futuro é criá-lo.” – Alan Kay*
