# Pseudocódigo de `classe base.py`

## 1) Classe base: `Conta_bancaria`
- Criar conta com:
  - número da conta
  - titular
  - saldo inicial 0
- `depositar(valor)`:
  - se `valor > 0`: somar ao saldo e mostrar mensagem
  - senão: mostrar erro de valor inválido
- `Mostrar_Saldo()`:
  - mostrar titular, número da conta e saldo com 2 casas decimais

## 2) Conta Corrente (herda `Conta_bancaria`)
- Construtor adiciona `limite` (padrão 500)
- `sacar(valor)`:
  - se `valor <= saldo + limite`: descontar do saldo e mostrar mensagem
  - senão: mostrar "saldo insuficiente"

## 3) Conta Poupança (herda `Conta_bancaria`)
- `sacar(valor)`:
  - se `valor <= saldo`: descontar e mostrar mensagem
  - senão: mostrar "saldo insuficiente"
- `render()`:
  - calcular juros (5% do saldo)
  - somar juros ao saldo
  - mostrar quanto rendeu

## 4) Execução (quando o arquivo é executado)
- Pedir ao usuário nome e número para criar conta corrente e poupança
- Para cada conta:
  - pedir depósito e aplicar
  - (para poupança) aplicar rendimento
  - pedir saque e aplicar
  - mostrar saldo final
