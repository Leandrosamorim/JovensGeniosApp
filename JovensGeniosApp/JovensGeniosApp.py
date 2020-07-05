import json
import time
from shutil import get_terminal_size

def perguntar(pergunta):
    print("\n" + pergunta)
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
    if correta.lower == opt.lower:
        print("Parabéns, você acertou!")
        return 1
    else:
        print("Sinto muito, você errou!")
        return 0

def inicio():
    premio = ["mil", "dois mil", "tres mil", "quatro mil", "cinco mil" , "dez mil", "vinte mil", "trinta mil", "quarenta mil", "cinquenta mil", "cem mil", "duzentos mil", "trezentos mil", "quatrocentos mil", "quinhentos mil", "um milhão"]
    perguntas = carregarPerguntas('lib/worldgk.json')
    i = 0

    for key, meta in perguntas.items():
        print("A pergunta número " + key + " valendo " + premio[i] + " reais")
        resposta = perguntar(meta["question"])


        if (not verifica(resposta, meta)):
            opt = input("Deseja reiniciar o jogo?\n(Digite 's' ou 'y' para confirmar)\n")
            if(opt == 'y' or opt == 's'):
                execute()
            else:
                exit


        i = i + 1


def execute():
    print("\n" * get_terminal_size().lines, end='')
    inicio()


if __name__ == '__main__':
    execute()