# 🏦 Banco Digital — Orientação a Objetos com Python

Projeto educacional em Python que simula operações bancárias básicas utilizando os pilares da **Programação Orientada a Objetos**: herança, encapsulamento e polimorfismo.

---

## 📌 Sobre o Projeto

Este projeto implementa um sistema bancário simples via terminal, com suporte a **Conta Corrente** e **Conta Poupança**, cobrindo operações de depósito, saque e rendimento.

---

## ✨ Funcionalidades

- ✅ Criação de conta com titular e número
- ✅ Depósito com validação de valor
- ✅ Saque com controle de saldo e limite
- ✅ Rendimento automático de 5% para poupança
- ✅ Exibição de saldo formatado

---

## 🗂️ Estrutura das Classes

```
ContaBancaria               ← Classe base
├── depositar(valor)
└── mostrar_saldo()

ContaCorrente(ContaBancaria)
└── sacar(valor)            ← Usa saldo + limite (padrão R$ 500)

ContaPoupanca(ContaBancaria)
├── sacar(valor)            ← Usa apenas o saldo
└── render()                ← Aplica juros de 5%
```

---

## 🔍 Pseudocódigo

### Classe base — `ContaBancaria`

```
Criar conta com:
  - número da conta
  - titular
  - saldo inicial = 0

depositar(valor):
  se valor > 0 → somar ao saldo e exibir confirmação
  senão        → exibir erro

mostrar_saldo():
  exibir titular, número da conta e saldo (2 casas decimais)
```

### `ContaCorrente` — herda `ContaBancaria`

```
Construtor adiciona: limite (padrão = 500)

sacar(valor):
  se valor <= saldo + limite → descontar do saldo e confirmar
  senão                      → exibir "saldo insuficiente"
```

### `ContaPoupanca` — herda `ContaBancaria`

```
sacar(valor):
  se valor <= saldo → descontar e confirmar
  senão             → exibir "saldo insuficiente"

render():
  juros = saldo * 0.05
  saldo += juros
  exibir quanto rendeu
```

### Execução principal

```
Para cada tipo de conta (Corrente e Poupança):
  1. Solicitar nome do titular e número da conta
  2. Solicitar valor de depósito e aplicar
  3. (Poupança) Aplicar rendimento
  4. Solicitar valor de saque e aplicar
  5. Exibir saldo final
```

---

## 🚀 Como Executar

**Pré-requisito:** Python 3.9+

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/banco-digital-streamlit.git

# Acesse a pasta
cd banco-digital-streamlit

# Execute o arquivo
python classe_base.py
```

---

## 📚 Conceitos Abordados

| Conceito | Aplicação |
|---|---|
| **Herança** | `ContaCorrente` e `ContaPoupanca` herdam de `ContaBancaria` |
| **Encapsulamento** | Saldo protegido, alterado apenas por métodos |
| **Polimorfismo** | Método `sacar()` com comportamento diferente em cada subclasse |
| **Abstração** | Interface comum via classe base |

---

## 👤 Autor

Feito com ❤️ para fins educacionais.

---

## 📄 Licença

Este projeto está sob a licença [MIT](LICENSE).
