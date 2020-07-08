import json
import time
from shutil import get_terminal_size

ajuda = 3
skip = 3
pts = 0
skiped = False

def perguntar(pergunta):
    print("\n" + pergunta["question"])
    global ajuda
    global skip
    global skiped

    if ajuda > 0 or skip > 0:
        print("Você pode: \n")
        if ajuda > 0:
            print("-Pedir ajuda aos universitários " + str(ajuda) + " vezes \n")
        if skip > 0:
            print("-Pular " + str(skip) + " vezes \n" )
        au = input("Pressione 'U' para ajuda dos universitários ou 'P' para pular. Se não precisar de ajuda, pressione 'N' \n")
        if (au == 'U' or au == 'u'):
            if(ajuda>0):
                ajuda = ajuda - 1
                print(pergunta["ajuda"] + "\n")
            else:
                print("Não pode mais pedir ajuda! \n")
        if au == 'P' or au == 'p':
            if skip > 0:
                skip = skip -1
                print("Próxima pergunta...")
                skiped = True
                return("p")
            else:
                print("Não pode mais pular! \n")

    opt = input("Qual a opção correta? [a/b/c/d]: ")

    while(True):
        if opt.lower() in ['a', 'b', 'c', 'd']:
            return opt
        else:
            print("Opção inválida, escolha novamente")
            opt = input("Escolha uma das opções [a/b/c/d]: ")

def carregarPerguntas(file):
    perguntas = None
    with open(file, "r") as r:
        perguntas = json.load(r)
    return (perguntas)

def verifica(opt, meta):
    correta = meta["answer"]
    global pts
    if correta.lower == opt.lower:
        print("Parabéns, você acertou!")
        pts = pts + 1
        return 1
    elif opt.lower == 'p':
        return 1
    else:
        print("Sinto muito, você errou!")
        return 0

def inicio():
    global pts
    global skiped
    premio = ["mil", "dois mil", "tres mil", "quatro mil", "cinco mil" , "dez mil", "vinte mil", "trinta mil", "quarenta mil", "cinquenta mil", "cem mil", "duzentos mil", "trezentos mil", "quatrocentos mil", "quinhentos mil", "um milhão"]
    perguntas = carregarPerguntas('lib/worldgk.json')
    i = 0

    for key, meta in perguntas.items():
        print("A pergunta número " + key + " valendo " + premio[pts] + " reais é:")
        time.sleep(3)
        resposta = perguntar(meta)

        if skiped == True:
            skiped = False
            continue
        print("\n" * get_terminal_size().lines * 2, end='')
        if (not verifica(resposta, meta)):
            opt = input("Deseja reiniciar o jogo? \n [pressione s ou y para confirmar, ou pressione qualquer tecla para sair]\n")
            if(opt == 'y' or opt == 's'):
                execute()
            else:
                quit()
        if pts == 16:
            print("\n" * get_terminal_size().lines * 2, end='')
            print("Parabéns, você acaba de ganhar um milhão de reais!")


        i = i + 1

def welcome():
    opt = input("Seja bem-vindo ao Show do Milhão! \n Deseja iniciar o jogo? [s/n]")
    if opt == 's':
        print("\n" * get_terminal_size().lines * 2, end='')
        inicio()
    else:
        exit()


def execute():
    welcome()


if __name__ == '__main__':
    execute()