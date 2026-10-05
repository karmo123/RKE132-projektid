from colorama import Fore, Style

# Kirjuta programm, mis küsib kasutajalt tema lemmikvärvi
# ja väljastab selle põhjal tema temperamendi.

# punane -> energiline
# roosa -> romantik
# roheline -> rahulik
# sinine -> keskendunud
# muu -> imeline üksarvik

color = input("Sisesta oma lemmikvärv:").lower()

match color:
    case "punane":
        print(Fore.RED + "Sa oled energiline inimene!" + Style.RESET_ALL)
    case "roosa":
        print(Fore.MAGENTA + "Sa oled romantik!" + Style.RESET_ALL)
    case "roheline":
        print(Fore.GREEN + "Sa oled rahulik inimene!" + Style.RESET_ALL)
    case "sinine":
        print(Fore.BLUE + "Sa oled keskendunud inimene!" + Style.RESET_ALL)
    case _:
        print(Fore.CYAN + "Sa oled imeline üksarvik!" + Style.RESET_ALL)