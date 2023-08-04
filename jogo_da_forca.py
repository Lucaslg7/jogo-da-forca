# Jogo da forca de Lucas Gabriel Mozinho da Silva

import random
import time

palavras = {
    'comida': ['maça', 'uva', 'Abacate', 'Abacaxi', 'Acerola', 'Banana Maça', 'Caju', 'Cereja', 'Figo', 'Framboesa',
               'Goiaba', 'Kiwi',
               'Laranja', 'Limao', 'Mamao', 'Melao', 'Pessego', 'Tangerina'], 'cor': ['vermelho', 'verde', 'rosa'],
    'objeto': ['recipiente', 'maçaneta', 'lapis', 'Ampulheta', 'Anzol', 'Bide', 'Botija', 'Candelabro',
               'Desfibrilador', 'Fantoche', 'Freezer', 'Navalha', 'Jaleco', 'Modem', 'Narguile', 'Nebulizador',
               'Oxímetro', 'Pendulo', 'Sintetizador', 'Spray', 'Webcam', 'Xadrez', 'Xilofone', 'Ziper'],
    'corpo humano': ['timo', 'traqueia', 'biceps', 'olho', 'dente', 'musculo', 'estomago', 'rim', 'perna', 'braço',
                     'mao', 'pulmao', 'coraçao', 'esofago', 'cartilagem', 'osso', 'dedo', 'unha', 'cabelo',
                     'articulaçao', 'baço', 'instestino delgado', 'intestino grosso', 'reto', 'joelho', 'patela',
                     'quadril', 'abdomem', 'pelo', 'cerebro', 'tireoide', 'nariz', 'laringe', 'faringe', 'garganta',
                     'amigdalas', 'palpebra', 'cilio', 'duodeno', 'bochecha', 'ombro', 'nervo', 'linfa', 'pescoço',
                     'pele', 'epiderme', 'derme', 'celula', 'mitocondria', 'ateria', 'veia', 'capilar'],
    'profissão': ['gari', 'medico', 'Apicultor', 'Agronomo', 'Auditor', 'Bartender', 'Cerimonialista', 'Chef',
                  'Coach', 'Desembargador', 'Despachante', 'Endocrinologista', 'Embaixador', 'Gerentologo',
                  'Interprete', 'Juiz', 'Nanotecnologo', 'Nutrologo', 'Pizzaiolo', 'Perito', 'Quiroprata',
                  'Roteirizador', 'Silvicultor', 'Taquigrafo', 'Turismologo'],
    'elemento químico': ['tantalo', 'ouro', 'litio', 'sodio', 'potassio', 'rubidio', 'cesio', 'francio', 'berilio',
                         'magnesio', 'calcio', 'estroncio', 'bario', 'radio', 'carbono', 'silício', 'germanio',
                         'estanho', 'chumbo', 'flerovio'], 'animal': ['Tamandua', 'abelha'],
    'nome': ['Bruna', 'Lucas', 'Alyssa', 'Kayke', 'Mariana', 'Lavegue'],
    'aleatório': ['Afobado', 'Amendoim', 'Banheiro', 'Caatinga', 'Cachorro', 'Campeonato', 'Capricornio',
                  'Catapora', 'Corrupçao', 'Crepusculo', 'Empenhado', 'Esparadrapo', 'Forca', 'Galaxia',
                  'Historia', 'Magenta', 'Manjericao', 'Menta', 'Moeda', 'Oraçao', 'Paçoca', 'Palavra',
                  'Pedreiro', 'Pneumonia', 'Pulmao', 'Rotatoria', 'Serenata', 'Transeunte', 'Trilogia',
                  'Xicara', 'alfazema']}

temas = ['comida', 'cor', 'objeto', 'corpo humano', 'profissão', 'elemento químico', 'animal', 'nome', 'aleatório']
hard_words = ['Paralelepípedo', 'Prognósticio', 'Acender', 'Afilhado', 'Ardiloso', 'Áspero',
              'Assombração', 'Asterisco', 'Basquete', 'Caminho', 'Champanhe', 'Chiclete', 'Chuveiro', 'Coelho',
              'Contexto', 'Convivência', 'Coração', 'Desalmado', 'Eloquente', 'Esfirra', 'Esquerdo', 'Exceção',
              'Fugaz', 'Gororoba', 'Heterossexual', 'Horrorizado', 'Impacto', 'Independência', 'Modernidade',
              'Oftalmologista', 'Otorrinolaringologista', 'Pororoca', 'Quarentena', 'Quimera', 'Refeição',
              'Reportagem', 'Sino', 'Taciturno', 'Tênue', 'Visceral']
boneco = ['''
_____
|  |
|  O
| /|\\
|  |
| / \\
''', '''
_____
|  |
|  O
| /|\\
|  |
| /''', '''
_____
|  |
|  O
| /|\\
|  |
|''', '''
_____
|  |
|  O
| /|\\
|  
|''', '''
_____
|  |
|  O
| /|
|  
|''', '''
_____
|  |
|  O
|  |
|
|''', '''
_____
|  |
|  O
|
|
|''', '''
_____
|  |
|
|
|
|''']


def MainMenu():
    option = 0
    mode = 0
    print('\n\nOlá, seja bem vindo ao nosso jogo da forca!')
    print('Este daqui é o menu principal, onde você poderá navegar pelo o nosso jogo da forca\n')
    print('Digite um dos números abaixo para acessar o campo desejado: ')
    print('''
    1 - Jogar
    2 - Como Jogar
    3 - Sair
    \n''')
    while option not in [1, 2, 3]:
        option = int(input('O que você quer fazer? '))
        if option == 1:
            while mode != 1 and mode != 2:
                mode = int(input('''Qual modo de jogo deseja jogar?
    1 - Modo normal
    2 - Modo hard
    3 - Voltar
'''))
                if mode == 1:
                    return Game()
                if mode == 2:
                    return HardMode()
                if mode == 3:
                    return MainMenu()
                else:
                    print('Selecione um modo válido!')
        elif option == 2:
            HowPlay()
        elif option == 3:
            return
        else:
            print('Digite uma opção válida')


def H_AnotherMatch():
    match = input('\nDigite "s" se quiser ir mais uma partida, ou digite "n" para voltar ao menu principal. ').lower()
    if match == 's':
        return HardMode()
    elif match == 'n':
        return MainMenu()
    else:
        print('Digite a letra correta para continuar')
        return H_AnotherMatch()


def AnotherMatch():
    match = input('\nDigite "s" se quiser ir mais uma partida, ou digite "n" para voltar ao menu principal. ').lower()
    if match == 's':
        return Game()
    elif match == 'n':
        return MainMenu()
    else:
        print('Digite a letra correta para continuar')


def ChoiceWord():
    l_word = []
    theme = random.choice(temas)
    word = random.choice(palavras[theme])
    for i in word:
        l_word.append(i.upper())
    return theme, l_word


def ChoiceHard():
    l_word = []
    h_word = random.choice(hard_words)
    for i in h_word:
        l_word.append(i.upper())
    return l_word


def HowPlay():
    time.sleep(2)
    print('\n1 - O objetivo deste jogo é descobrir uma palavra adivinhando as letras que ela possui. A cada rodada,\n '
          'os jogadores irão simultaneamente escolher uma letra que suspeitem fazer parte da palavra. Caso a palavra\n '
          'contenha esta letra, será mostrado em que posição(ões) ela está. Entretanto, caso esta letra não exista '
          'na\n '
          'palavra, será desenhada uma parte do corpo do boneco do jogador. Se todas as 7 partes do corpo do boneco\n '
          'estiverem desenhadas, o jogador estará fora da partida.')
    print('2 - Digite apenas uma letra por vez')
    print('3 - Não digite números')
    print('4 - No modo normal, as palavras não tem acento, já no modo dificil, as palavras possuem acentuação, então '
          'cuidado!')
    print('5 - Divirta-se :)')
    print()
    back = input('Digite qualquer letra para voltar ao menu principal ').lower()
    return MainMenu()


def HardMode():
    tentativas = 7
    wrong_letters = []
    tema = 'Modo Hard'
    palavra = ChoiceHard()
    palavra1 = palavra.copy()
    correct_word = []
    for i in palavra:
        if i.isalpha():
            correct_word.append('_ ')
        else:
            correct_word.append(i)
    print('Carregando jogo...')
    time.sleep(2)
    while tentativas > 0:
        if correct_word != palavra1:
            print('=' * 50)
            print(str.center(tema, 50, ' '))
            print('=' * 50)
            print('Letras erradas:', wrong_letters)
            print(boneco[tentativas], end='')
            print(' ' * 25, *correct_word, ' ' * 25)
            print()
            letter = input('Digite uma letra: ').upper()
            if letter.isalpha():
                if letter in wrong_letters or letter in correct_word:
                    print('Letra já usada')
                    time.sleep(2)
                elif letter in palavra:
                    if palavra.count(letter) < 2:
                        correct_word[palavra.index(letter)] = palavra[palavra.index(letter)]
                    else:
                        for i in range(palavra.count(letter)):
                            correct_word[palavra.index(letter)] = palavra[palavra.index(letter)]
                            palavra[palavra.index(letter)] = '-'
                else:
                    wrong_letters.append(letter)
                    tentativas -= 3
            elif letter.isnumeric():
                print('Digite apenas letras.')
                time.sleep(2)
        else:
            print('=' * 50)
            print(str.center(f'TEMA: {tema}', 50, ' '))
            print('=' * 50)
            print('Letras erradas:', wrong_letters)
            print(boneco[tentativas], end='')
            print(' ' * 25, *correct_word, ' ' * 25)
            print()
            print(f'\n\nParabéns!!!\nVocê acertou a palavra corretamente.\n Deseja ir outra partida? ')
            return H_AnotherMatch()
    else:
        print('=' * 50)
        print(str.center(f'TEMA: {tema}', 50, ' '))
        print('=' * 50)
        print('Letras erradas:', wrong_letters)
        print(boneco[0], end='')
        print(' ' * 25, *correct_word, ' ' * 25)
        print()
        print('Voce perdeu!')
        return H_AnotherMatch()


def Game():
    tentativas = 7
    wrong_letters = []
    tema, palavra = ChoiceWord()
    palavra1 = palavra.copy()
    correct_word = []
    for i in palavra:
        if i.isalpha():
            correct_word.append('_ ')
        else:
            correct_word.append(i)
    print('Carregando jogo...')
    time.sleep(2)
    while tentativas > 0:
        if correct_word != palavra1:
            print('=' * 50)
            print(str.center(f'TEMA: {tema}', 50, ' '))
            print('=' * 50)
            print('Letras erradas:', wrong_letters)
            print(boneco[tentativas], end='')
            print(' ' * 25, *correct_word, ' ' * 25)
            print()
            letter = input('Digite uma letra: ').upper()
            if letter.isalpha():
                if letter in wrong_letters or letter in correct_word:
                    print('Letra já usada')
                    time.sleep(2)
                elif letter in palavra:
                    if palavra.count(letter) < 2:
                        correct_word[palavra.index(letter)] = palavra[palavra.index(letter)]
                    else:
                        for i in range(palavra.count(letter)):
                            correct_word[palavra.index(letter)] = palavra[palavra.index(letter)]
                            palavra[palavra.index(letter)] = '-'
                else:
                    wrong_letters.append(letter)
                    tentativas -= 1
            elif letter.isnumeric():
                print('Digite apenas letras.')
                time.sleep(2)
        else:
            print('=' * 50)
            print(str.center(f'TEMA: {tema}', 50, ' '))
            print('=' * 50)
            print('Letras erradas:', wrong_letters)
            print(boneco[tentativas], end='')
            print(' ' * 25, *correct_word, ' ' * 25)
            print()
            print(f'\n\nParabéns!!!\nVocê acertou a palavra corretamente.\n Deseja ir outra partida? ')
            return AnotherMatch()
    else:
        print('=' * 50)
        print(str.center(f'TEMA: {tema}', 50, ' '))
        print('=' * 50)
        print('Letras erradas:', wrong_letters)
        print(boneco[tentativas], end='')
        print(' ' * 25, *correct_word, ' ' * 25)
        print()
        print('Voce perdeu!')
        return AnotherMatch()

1
# Corpo Principal

MainMenu()
