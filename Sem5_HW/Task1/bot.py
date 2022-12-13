import user_inteface as ui
import model
import random


def enemy_turn():
    if 0 < model.get_current_set_candys() < 29:
        taken_candy = model.get_current_set_candys()
        model.set_current_set_candys(taken_candy)
        ui.set_history(taken_candy, False)
    model.check_win()
    if model.get_current_set_candys() == 150:
        taken_candy = 5
        model.set_current_set_candys(taken_candy)
        ui.set_history(taken_candy, False)
    elif model.get_current_set_candys() > 28:
        if model.get_current_set_candys() % 29 != 0:
            taken_candy = model.get_current_set_candys() - int((model.get_current_set_candys() // 29) * 29)
        else:
            taken_candy = random.randint(1, 29)
        model.set_current_set_candys(taken_candy)
        ui.set_history(taken_candy, False)
        # model.switch_turn()
