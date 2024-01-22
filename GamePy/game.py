from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

# método para receber a dificuldade
def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade) # instaciando um objeto e passasndo a dificuldade como parâmetro

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao() # apresentando a operação

    resultado: int = int(input()) # informando resultado

    # checando resultado
    if calc.checar_resultado(resultado): 
        pontos += 1 # para True, soma-se 1 ponto
        print(f'Você tem {pontos} ponto(s).')

    # continuar ou não, independente do resultado
    continuar: int = int(input('Deseja continuar no jogo? [1-sim, 0-não]: '))

    # para sim, executa-se novamente a função 'jogar'
    if continuar:
        jogar(pontos)
    else: # para não, finaliza
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
    