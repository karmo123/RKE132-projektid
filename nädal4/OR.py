username = input("Sisesta kasutajanimi:")
password = input("Sisesta parool:")

if username != "user" or password != "1234":
    print("Access denied!")
else:
    print("Welcome!")