# Sistema Bancário Modularizado

Um sistema bancário simples desenvolvido em Python que demonstra conceitos de programação funcional e modularização de código.

## 📋 Funcionalidades

### Operações Bancárias Básicas
- **Depósito**: Adicionar valores à conta
- **Saque**: Retirar valores com validações de limite e saldo
- **Extrato**: Visualizar histórico de transações e saldo atual

### Gestão de Usuários e Contas
- **Cadastro de Usuário**: Registrar clientes com dados pessoais completos
- **Criação de Conta**: Vincular contas correntes a usuários existentes
- **Listagem de Contas**: Exibir todas as contas cadastradas no sistema

## 🚀 Como Usar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sistema-bancario.git
cd sistema-bancario
```

2. Execute o programa:
```bash
python sistema_bancario.py
```

3. Use o menu interativo para navegar pelas funcionalidades.

## 🏗️ Arquitetura

O sistema foi desenvolvido seguindo princípios de programação funcional com separação clara de responsabilidades:

### Funções Principais

- `sacar()`: Utiliza argumentos nomeados obrigatórios (keyword-only)
- `depositar()`: Utiliza argumentos posicionais obrigatórios (positional-only)  
- `exibir_extrato()`: Combina argumentos posicionais e nomeados
- `criar_usuario()`: Gerencia cadastro de clientes
- `criar_conta()`: Cria contas vinculadas a usuários
- `listar_contas()`: Exibe informações das contas

## 💾 Estrutura de Dados

### Usuário
```python
{
    "nome": str,
    "data_nascimento": str,
    "cpf": str,
    "endereco": str
}
```

### Conta Corrente
```python
{
    "agencia": "0001",
    "numero_conta": int,
    "usuario": dict
}
```

## ⚡ Validações Implementadas

- **CPF único**: Impede cadastro de usuários duplicados
- **Limite de saque**: R$ 500,00 por operação
- **Limite diário**: Máximo 3 saques por dia
- **Validação de saldo**: Impede saques sem saldo suficiente
- **Valores positivos**: Apenas valores válidos para depósitos e saques

## 🔧 Recursos Técnicos

- **Modularização**: Código organizado em funções especializadas
- **Argumentos tipificados**: Uso correto de `*` e `**` para controle de parâmetros
- **Validação robusta**: Múltiplas camadas de verificação
- **Interface amigável**: Menu interativo e mensagens claras

## 📝 Exemplo de Uso

```
================ MENU ================
[d]     Depositar
[s]     Sacar
[e]     Extrato
[nu]    Novo usuário
[nc]    Nova conta
[lc]    Listar contas
[q]     Sair
=> 
```

## 🎯 Conceitos Demonstrados

- Programação funcional em Python
- Separação de responsabilidades
- Validação de dados
- Estruturas de dados simples
- Interface de linha de comando
- Controle de argumentos de função

## 📊 Status do Projeto

✅ Funcionalidades básicas implementadas  
✅ Sistema de usuários e contas  
✅ Validações de segurança  
⏳ Possíveis melhorias futuras: persistência de dados, interface gráfica

---

**Desenvolvido como projeto educacional para demonstrar boas práticas de programação em Python.**
