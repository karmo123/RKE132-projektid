# Kirjuta programm, mis küsib kasutajalt tema lemmikvärvi
# ja väljastab selle põhjal tema temperamendi.

# punane -> energiline
# roosa -> romantik
# roheline -> rahulik
# sinine -> keskendunud
# muu -> imeline üksarvik

color = input("Sisesta oma lemmikvärv:").lower()

# if color == "punane":
#     print("Sa oled energiline inimene!")
# elif color == "roosa":
#     print("Sa oled romantik!")
# elif color == "roheline":
#     print("Sa oled rahulik inimene!")
# elif color == "sinine":
#     print("Sa oled keskendunud inimene!")
# else:
#     print("Sa oled imeline üksarvik!")

match color:
    case "punane":
        print("Sa oled energiline inimene!")
    case "roosa":
        print("Sa oled romantik!")
    case "roheline":
        print("Sa oled rahulik inimene!")
    case "sinine":
        print("Sa oled keskendunud inimene!")
    case _:
        print("Sa oled imeline üksarvik!")