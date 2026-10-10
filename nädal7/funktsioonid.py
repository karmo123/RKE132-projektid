import datetime


def get_greeting():
    hour = datetime.datetime.now().hour

    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def say_hello():
    name = input("Enter your first name: ")
    greeting = get_greeting()

    print(f"{greeting}, {name}!")


say_hello()