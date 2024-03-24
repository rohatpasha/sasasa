import random
import time

print("Bu bir şifre oluşturucu programdr")
sfd=int(input("Kaç haneli bir şifre olsun?"))

asd = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

şifre = "%4"
time.sleep(4)
for i in range(sfd):
    şifre += random.choice(asd)
    print(şifre)
