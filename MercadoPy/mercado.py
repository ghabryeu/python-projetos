from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

# menu
def menu() -> None:
    print('Bem-vindo(a)!')
    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar produto.')
    print('2 - Listar produto.')
    print('3 - Comprar produto.')
    print('4 - Visualizar carrinho.')
    print('5 - Fechar pedido.')
    print('6 - Sair do sistema.')

    opcao: int = int(input())

    # definindo as opções
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()

# cadastrando produtos
def cadastrar_produto() -> None:
    print('Cadastro de Produto')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()

# apresentar produtos
def listar_produto() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')

        for produto in produtos:
            print(produto)
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()

# dando baixa no produto
def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto: ')

        print('Produtos Disponíveis')
        for produto in produtos:
            print(produto)
            sleep(1)
        codigo: int = int(input())

        # seleção de produto pelo usuário
        produto: Produto = pega_produto_por_codigo(codigo)

        # verificando se há produto no carrinho
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                # adicionando a quantidade do produto
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos cadastrados!')
    sleep(2)
    menu()

# visualizando produtos
def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                sleep(1)
                menu()
    else:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()

# fechando o pedido
def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(1)
    menu()

# código do produto
def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
        return p 

if __name__ == '__main__':
    main()
    