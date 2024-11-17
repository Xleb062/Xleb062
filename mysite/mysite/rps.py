"""
rockpapersscissors
"""
import random

options = ['rock', 'paper','scissors']
player_choise = ''


while player_choise!='q':
    player_choise = input('Введите rock,paper,scissors: ')
    if player_choise not in options:
        print('некорректный ввод')
        continue
    pk_choise = random.choice(options)
    print('player: ', player_choise, '-', pk_choise,'computer' )

    if player_choise == 'rock'and pk_choise =="rock" or player_choise == 'paper'and pk_choise =="paper" or player_choise == 'scissors'and pk_choise =="scissors":
        print('ничья')
    elif player_choise == 'rock' and pk_choise =="scissors" or player_choise == 'scissors' and pk_choise =="paper"or player_choise == 'paper' and pk_choise =="rock":
        print("победил игрок")
    else:
        print('победил пк')

