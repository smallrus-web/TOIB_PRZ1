import re


def is_strong_password(password):
    if len(password) < 8:
        return False

    if not (re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'\d', password) and
            re.search(r'[!@#$%^&*()-_+=<>?/\\|{}[\]~]', password)):
        return False

    return True


def main():
    try:
        with open("password.txt", "r") as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print("Файл password.txt не найден в текущей директории.")
        return

    strong_passwords = [password for password in passwords if is_strong_password(password)]

    if strong_passwords:
        print("Следующие пароли соответствуют требованиям:")
        for password in strong_passwords:
            print(password)
    else:
        print("Нет паролей, соответствующих требованиям.")


if __name__ == "__main__":
    main()
