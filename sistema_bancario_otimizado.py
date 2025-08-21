def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Função para realizar saque com argumentos nomeados apenas."""
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        return saldo, extrato, numero_saques, "Operação falhou! Você não tem saldo suficiente."
    
    elif excedeu_limite:
        return saldo, extrato, numero_saques, "Operação falhou! O valor do saque excede o limite."
    
    elif excedeu_saques:
        return saldo, extrato, numero_saques, "Operação falhou! Número máximo de saques diários excedido."
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques, "Saque realizado com sucesso!"
    
    else:
        return saldo, extrato, numero_saques, "Operação falhou! O valor informado é inválido."


def depositar(saldo, valor, extrato):
    """Função para realizar depósito com argumentos posicionais."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato, "Depósito realizado com sucesso!"
    else:
        return saldo, extrato, "Operação falhou! O valor informado é inválido."


def exibir_extrato(saldo, *, extrato):
    """Função para exibir extrato com argumentos posicionais e nomeados."""
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    """Função para criar novo usuário (cliente)."""
    cpf = input("Informe o CPF (somente números): ")
    
    # Verificar se usuário já existe
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe usuário com esse CPF!")
            return usuarios
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    
    print("Usuário criado com sucesso!")
    return usuarios


def criar_conta(agencia, numero_conta, usuarios):
    """Função para criar nova conta corrente."""
    cpf = input("Informe o CPF do usuário: ")
    
    # Buscar usuário pelo CPF
    usuario = None
    for u in usuarios:
        if u["cpf"] == cpf:
            usuario = u
            break
    
    if usuario:
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
        print(f"Conta criada com sucesso! Agência: {agencia}, Conta: {numero_conta}")
        return conta
    else:
        print("Usuário não encontrado! Fluxo de criação de conta encerrado.")
        return None


def listar_contas(contas):
    """Função para listar todas as contas."""
    if not contas:
        print("Não há contas cadastradas.")
        return
    
    for conta in contas:
        linha = f"Agência:\t{conta['agencia']}\nC/C:\t\t{conta['numero_conta']}\nTitular:\t{conta['usuario']['nome']}\n"
        print("=" * 50)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    menu = """
================ MENU ================
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[nu]\tNovo usuário
[nc]\tNova conta
[lc]\tListar contas
[q]\tSair
=> """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato, mensagem = depositar(saldo, valor, extrato)
            print(mensagem)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques, mensagem = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            print(mensagem)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            usuarios = criar_usuario(usuarios)

        elif opcao == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar nosso sistema bancário. Volte sempre!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()