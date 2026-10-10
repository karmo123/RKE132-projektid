# Kirjutage programm, mis käib läbi iga tähe sõnes ja prindib selle välja.

text = "Python"

for letter in text:
    print(letter)

    text = "hello"

for i in text:
    print(i)

   

length = len(text)
print(length)

for letter in range(len(text) - 1, -1, -1):
    print(text[letter])