from classbook import contacts
from utils import edits


def main():
    try:
        while True:
            user_input = input("Введіть команду: ")
            res = edits(user_input)
            print(res)
            if res == "До наступної зустрічі":
                break
    finally:
        contacts.save_contacts_to_file()

if __name__ == "__main__":
    main()