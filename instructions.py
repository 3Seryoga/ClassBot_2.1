from commands import (first_step, add_contacts, change_phone_funk, find_phone, show_all_funk, quit_funk, del_phone_funk,
                      del_funk, birthday_funk, next_birthday_funk)

COMMANDS = {
    "hello": first_step,
    "add": add_contacts,
    "change phones": change_phone_funk,
    "phone": find_phone,
    "show all": show_all_funk,
    "good bye": quit_funk,
    "close": quit_funk,
    "exit": quit_funk,
    "delete phone": del_phone_funk,
    "delete": del_funk,
    "birthday": birthday_funk,
    "days to birthday": next_birthday_funk,

}
