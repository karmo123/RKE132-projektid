def read_data():
    file_path = r"data\weapons.txt"

    with open(file_path, "r", encoding="utf-8") as f:
        data = f.readlines()
        print(data)


read_data()