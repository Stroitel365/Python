"""
Создайте программу для игры с конфетами человек против компьютера.
Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота "интеллектом"
"""

import random
import user_inteface as ui

set_candys = 150
current_set_candys = 150
turn = None
turn_init = ''


def get_first_move() -> bool:
    global turn_init
    turn_init = random.randint(0, 1)
    if turn_init == 1:
        set_first_move(True)
        turn_init = True
    else:
        set_first_move(False)
        turn_init = False
    return turn_init


def set_first_move(turn_init: bool):  # true - играет человек, false - играет комп
    global turn
    turn = turn_init


# def switch_turn():
#     global turn
#     turn = not turn


def check_win():
    global current_set_candys
    if current_set_candys == 0:
        ui.set_wining(turn)
        current_set_candys = False


def get_current_set_candys():
    global current_set_candys
    return current_set_candys


def set_current_set_candys(taken):
    global current_set_candys
    current_set_candys -= taken


def player_turn(taken_candy):
    set_current_set_candys(taken_candy)
    ui.set_history(taken_candy, True)
    check_win()
    # switch_turn()
