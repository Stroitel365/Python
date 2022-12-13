from tkinter import *
import model
# import controller as ct
import time
import bot

history = "История ходов: \n"


def hide_button(widget):
    # This will remove the widget from toplevel
    widget.grid_forget()


def start_button():
    global txt_window, txt_history, button_enter, txt_count_down, button_start, lbl_task, window
    turn_init = model.get_first_move()
    if turn_init:
        button_start.configure(text='Первый ходите Вы\n (нажмите для продолжения)')
    else:
        button_start.configure(text='Первый ходит компьютер\n (нажмите для продолжения)')
    button_start.configure(command=lambda: hide_button(button_start))
    lbl_task.grid_forget()
    lbl_enter = Label(window,
                      text="Введите кол-во забираемых конфет\n"
                           "от 1 до 28 шт.",
                      font=("Arial Bold", 10))
    lbl_enter.grid(column=1, row=4)
    txt_window.grid(column=2, row=4)
    button_enter.grid(column=3, row=4)
    button_enter.configure(command=lambda: play_button())
    txt_history.grid(column=1, row=5)
    txt_count_down.grid(column=2, row=5)
    window.geometry("500x300")
    while type(model.get_current_set_candys()) == int:
        if turn_init:
            play_button()
            bot.enemy_turn()
        else:
            bot.enemy_turn()
            play_button()


def play_button():
    global txt_window
    taken_candy = int(txt_window.get())
    if taken_candy > 28 or taken_candy <= 0 or taken_candy > model.get_current_set_candys():
        txt_error = Label(window, text="Неправильное кол-во конфет!", font=("Arial Bold", 8))
        txt_error.grid(column=2, row=3)
        time.sleep(5)
        hide_button(txt_error)
    else:
        model.player_turn(taken_candy)
    bot.enemy_turn()
    # model.switch_turn()


def set_wining(turn):
    if turn:
        lbl_win = Label(window,
                        text="Вы победили!",
                        font=("Arial Bold", 20))
        lbl_win.grid(column=1, row=6)
    else:
        lbl_win = Label(window,
                        text="Компьютер победил!",
                        font=("Arial Bold", 20))
        lbl_win.grid(column=1, row=6)


def set_history(taken_candy, whos_turn):
    global txt_history, txt_count_down, history
    if whos_turn:
        who = "HUMAN"
    else:
        who = "COMP"
    history += f"{who} взял {taken_candy}\n"
    txt_history.configure(text=history)
    txt_count_down.configure(text=f"{model.get_current_set_candys()} конфет осталось")


def set_interface():
    global txt_window, txt_history, button_enter, txt_count_down, button_start, lbl_task, window
    window = Tk()
    window.title("Добро пожаловать в приложение 'Заберу твои конфеты' ")
    window.geometry("500x200")
    txt_window = Entry(window, width=20)
    txt_window.grid_forget()
    txt_history = Label(window, text="История ходов: \n")
    txt_history.grid_forget()
    button_enter = Button(window, text="Ввод")
    button_enter.grid_forget()
    txt_count_down = Label(window, text="150 конфет осталось")
    txt_count_down.grid_forget()
    lbl_task = Label(window,
                     text="На столе лежит 150 конфет. Играют игрок против компьютера.\n "
                          "За один ход можно забрать от 1 до 28 конфет.\n"
                          "Первый ход определяется кнопкой.\n"
                          "Побеждает, кто забирает последнюю конфету",
                     font=("Arial Bold", 13))
    lbl_task.grid(column=2, row=1)
    button_start = Button(window, text="Start game", command=lambda: start_button())
    button_start.grid(column=2, row=5)
    window.mainloop()
