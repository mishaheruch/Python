import string
def password_validator():
    password = input("Enter a password: ")
    if ' ' in password:
        print("Error: Password must not contain spaces.")
        return
    if len(password) < 12:
        print("Error: Password must be at least 12 characters long.")
        return
    if len(password) > 40:
        print("Error: Password must be no more than 40 characters long.")
        return
    if not any(char.islower() for char in password):
        print("Error: Password must contain at least one lowercase letter.")
        return
    if not any(char.isupper() for char in password):
        print("Error: Password must contain at least one uppercase letter.")
        return
    if not any(char in string.punctuation for char in password):
        print("Error: Password must contain at least one special character.")
        return

    print("Password is valid.")
password_validator()
# Рома все зробив і даже бібліотеку string використав! бо щось isdigit() не хотіло робити в принципі має бути робочий код на всі вимоги Сидів з 6 і до 9:30 вечора!
# Але я не розумію чому він не використовує isdigit() для перевірки цифр, але в принципі все працює як треба.