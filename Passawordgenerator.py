import random
import time

print("Welcome To Passaword Generator")

chars='qwertyuıopğüişlkjhgfdsazxcvbnmöçQWERTYUIOPĞÜİŞLKJHGFDSAZXCVBNMÖÇ1234567890@>£#$½{[]}!^&%/()=?*é.()!:;¨'

number = int(input("How many passawords dou you wanna create? : "))

lenght=int(input("Passaword Lenght : "))


print("\nYour passawords Loading...")

for i in range(number):
    passawords=' '

    for j in range(lenght):
        passawords+=random.choice(chars)
        time.sleep(0.08)

    print("{} = {}".format(i+1,passawords))


