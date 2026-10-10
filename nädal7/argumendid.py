import datetime

hour = datetime.datetime.now().hour
name = input("Enter your first name: ")


def get_greeting(daytime):
    if daytime < 12:
        return "Good morning"
    elif daytime < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def say_hello(daytime, first_name):
    greeting = get_greeting(daytime)

    print(f"{greeting}, {first_name}!")


say_hello(hour, name)