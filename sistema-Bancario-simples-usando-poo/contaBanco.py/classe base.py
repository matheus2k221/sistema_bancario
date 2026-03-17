# ------------------------------------------------------------------
# 0. Mensagem de boas‑vindas
# ------------------------------------------------------------------
print("\n--- BEM VINDO AO SISTEMA BANCÁRIO DO BANCO 'MISTER' ---")
print("--- AQUI SEU DINHEIRO SOME EM UM PASSO DE MAGIA ---")

# ------------------------------------------------------------------
# 1. Definição das classes bancárias
# ------------------------------------------------------------------
class Conta_bancaria:
    def __init__(self, numero_conta, titular):
        # Atribui o número da conta e o nome do titular ao objeto
        self.numero_conta = numero_conta
        self.titular = titular
        # O saldo começa em 0 e usa o prefixo '_' para indicar que é um
        # atributo protegido (Encapsulamento), acessado apenas por métodos.
        self._saldo = 0  

    def depositar(self, valor):
        # Regra de negócio: só aceita valores positivos
        if valor > 0:
            self._saldo += valor
            # Exibe confirmação formatada com duas casas decimais (:.2f)
            print(f"Depósito de R$ {valor:.2f} realizado na conta de {self.titular}.")
        else:
            print("Valor de depósito inválido")

    def Mostrar_Saldo(self):
        # Exibe os dados atuais do objeto instanciado
        print(f"Titular: {self.titular} | Conta: {self.numero_conta} | Saldo: R$ {self._saldo:.2f}")


# A classe Conta_Corrente herda (recebe) as características da Conta_bancaria
class Conta_Corrente(Conta_bancaria):
    def __init__(self, numero_conta, titular, limite=500):
        # super() chama o construtor da classe pai para reaproveitar o código de criação
        super().__init__(numero_conta, titular)
        # Atributo exclusivo da conta corrente
        self.limite = limite

    def sacar(self, valor):
        # Polimorfismo: O saque aqui considera o saldo disponível + o limite extra
        if valor <= (self._saldo + self.limite):
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} aprovado (usando limite, se necessário).")
        else:
            print("Saldo insuficiente")


# A classe Conta_poupanca também herda de Conta_bancaria
class Conta_poupanca(Conta_bancaria):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)

    def sacar(self, valor):
        # Polimorfismo: Diferente da corrente, a poupança só saca o que tem em saldo
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado da poupança.")
        else:
            print("Saldo insuficiente")

    def render(self):
        # Método exclusivo para calcular 5% de juros sobre o saldo atual
        juros = self._saldo * 0.05
        self._saldo += juros
        print(f"Rendimento de R$ {juros:.2f} aplicado à poupança.")


# ------------------------------------------------------------------
# 4. Estrutura de armazenamento
# ------------------------------------------------------------------
# Dicionário usado como uma 'base de dados' temporária em memória
banco = {}

# ------------------------------------------------------------------
# 5. Funções auxiliares (Lógica do Sistema)
# ------------------------------------------------------------------
def cadastrar_conta():
    """Lógica para criar objetos e armazená-los no dicionário 'banco'."""
    print("\n--- CADASTRO DE NOVA CONTA ---")
    
    try:
        tipo = input("Tipo (C = Corrente, P = Poupança): ").strip().upper()
        titular = input("Nome do titular: ").strip()
        numero = int(input("Número da conta (inteiro): ").strip())

        # Verifica se a chave (número da conta) já existe no dicionário
        if numero in banco:
            print(f"Conta {numero} já existe. Operação cancelada.")
            return

        # Instanciação: Cria o objeto baseado na escolha do usuário
        if tipo == "C":
            conta = Conta_Corrente(numero, titular)
        elif tipo == "P":
            conta = Conta_poupanca(numero, titular)
        else:
            print("Tipo inválido. Use 'C' ou 'P'.")
            return

        # Guarda o objeto no dicionário usando o número como chave
        banco[numero] = conta
        print(f"Conta {numero} cadastrada com sucesso!")

        # Oferece uma facilidade para o usuário não precisar ir ao menu de operações
        opcao = input("Deseja fazer um depósito inicial? (S/N): ").strip().upper()
        if opcao == "S":
            valor = float(input("Valor do depósito inicial: R$ "))
            conta.depositar(valor)
            conta.Mostrar_Saldo()

    except ValueError:
        # Captura erros de conversão (ex: digitar letras no número da conta)
        print("Erro: Digite valores numéricos válidos. Operação cancelada.")

def consultar_conta():
    """Lógica de busca no dicionário e exibição de dados."""
    print("\n--- CONSULTA DE CONTA ---")
    try:
        numero = int(input("Número da conta: ").strip())
        # Tenta recuperar o objeto pela chave. Se não existir, retorna None.
        conta = banco.get(numero)

        if not conta:
            print(f"Nenhuma conta encontrada com o número {numero}.")
            opcao = input("Deseja cadastrar esta conta? (S/N): ").strip().upper()
            if opcao == "S":
                cadastrar_conta()
            return

        # Se encontrou, exibe as informações do objeto
        print(f"\nTitular: {conta.titular}")
        print(f"Número: {conta.numero_conta}")
        conta.Mostrar_Saldo()
        
        # Uso de isinstance para verificar o tipo do objeto e dar dicas específicas
        if isinstance(conta, Conta_poupanca):
            print("Esta é uma conta poupança. Use 'render' para aplicar juros.")
    except ValueError:
        print("Número de conta inválido.")

def operacoes_conta():
    """Menu secundário para transações financeiras em uma conta específica."""
    print("\n--- OPERAÇÕES NA CONTA ---")
    try:
        numero = int(input("Número da conta: ").strip())
        conta = banco.get(numero)

        if not conta:
            print(f"Nenhuma conta encontrada.")
            return

        # Loop de operações para que o usuário não precise digitar o número da conta toda hora
        while True:
            print(f"\nOperando: {conta.titular} (Conta: {conta.numero_conta})")
            print("[1] Depositar")
            print("[2] Sacar")
            # Só exibe a opção 3 se o objeto for do tipo Conta_poupanca
            if isinstance(conta, Conta_poupanca):
                print("[3] Render (poupança)")
            print("[4] Mostrar saldo")
            print("[0] Voltar")

            escolha = input("Opção: ").strip()
            if escolha == "1":
                valor = float(input("Valor: R$ "))
                conta.depositar(valor)
            elif escolha == "2":
                valor = float(input("Valor: R$ "))
                conta.sacar(valor)
            elif escolha == "3" and isinstance(conta, Conta_poupanca):
                conta.render()
            elif escolha == "4":
                conta.Mostrar_Saldo()
            elif escolha == "0":
                break # Sai do loop de operações e volta ao menu principal
    except ValueError:
        print("Valor numérico inválido.")

# ------------------------------------------------------------------
# 6. Loop principal (Interface com o Usuário)
# ------------------------------------------------------------------
def menu_principal():
    """Mantém o programa rodando até que o usuário decida sair."""
    while True:
        print("\n===== SISTEMA BANCÁRIO - MENU =====")
        print("[1] Cadastrar nova conta")
        print("[2] Consultar conta")
        print("[3] Operações na conta")
        print("[0] Sair")
        escolha = input("Selecione uma opção: ").strip()

        if escolha == "1":
            cadastrar_conta()
        elif escolha == "2":
            consultar_conta()
        elif escolha == "3":
            operacoes_conta()
        elif escolha == "0":
            print("Finalizando atendimento. Até logo!")
            break # Encerra o programa
        else:
            print("Opção inválida.")

# Ponto de entrada oficial do script
if __name__ == "__main__":
    menu_principal()