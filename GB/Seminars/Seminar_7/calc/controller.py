import user_interfeice as ui
import log_generate as lg
import model_racional as mr


def start_nums():
    user_nums, nums = ui.get_nums()
    lg.write_data(nums) # Запись данных которые ввел пользователь в лог
    result = mr.get_result(nums)
    lg.write_result(result)
    ui.print_user(user_nums, result)
