



def input_error(error):
    def wrapper(*args, **kwargs):
        try:
            return error(*args, **kwargs)
        except KeyError:
            return "Ви ввели не вірне ім'я"
        except IndexError:
            return "Потрібне ім'я та номер телефону"
        except ValueError as red:
            return red.args[0]

    return wrapper