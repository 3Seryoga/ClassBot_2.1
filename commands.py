from classbook import contacts, Record
from decorator import input_error


@input_error
def first_step():
    return "How can I help you?"


@input_error
def add_contacts(data):
    name, *phones = data.strip().split(" ")
    if name in contacts:
        raise ValueError("Дублікат імені")
    new_record = Record(name)

    for phone in phones:
        new_record.add_phone(phone)

    contacts.add_record(new_record)
    return f"Ви створили {name}:{phones}"


@input_error
def change_phone_funk(data):
    name, *phones = data.strip().split(" ")
    record = contacts[name]
    record.change_phones(phones)

    return "Телефон було змінено"

    #     return f"Для контакту {name} змінено номер на {phones}"
    return f"За даним {name} контакту не існує, зверніться до команди add "


@input_error
def find_phone(value):
    return contacts.search(value.strip()).get_info()


@input_error
def show_all_funk():
    contact = ""

    page_number = 1
    for page in contacts.iterator():
        contact += f"Page #{page_number}\n"

        for record in page:
            contact += f"{record.get_info()}\n"
        page_number += 1

    return contact


@input_error
def quit_funk():  # Функція виходу з команд "good bye", "close", "exit".
    return "До наступної зустрічі"


@input_error
def del_funk(name):
    name = name.strip()
    contacts.remove_record(name)
    return f"{name} видалено"


@input_error
def del_phone_funk(data):
    name, phone = data.strip().split(" ")

    record = contacts[name]
    if record.delete_phone(phone):
        return f"{phone} видалений"
    return f"{phone} номер відсутній "


@input_error
def birthday_funk(data):
    name, birthday_date = data.strip().split(" ")
    record = contacts[name]
    record.add_birthday(birthday_date)

    return f"{birthday_date} Дата дня народження створена"


def next_birthday_funk(name):
    name = name.strip()
    record = contacts[name]

    return f"День народження відбудеться через {record.get_days_to_next_birthday()} днів"
