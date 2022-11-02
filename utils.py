from instructions import COMMANDS



def return_func(data):
    return COMMANDS.get(data, error_func)

def error_func():
    return "Помилкова команда"

def edits(input_data):
    key_part = input_data
    data_part = ""
    for command in COMMANDS:
        if input_data.strip().lower().startswith(command):
            key_part = command
            data_part = input_data[len(key_part):]
            break
    if data_part:
        return return_func(key_part)(data_part)
    else:
        return return_func(key_part)()