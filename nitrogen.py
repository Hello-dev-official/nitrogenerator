import matplotlib.pyplot as plt
import requests
import random
import itertools
import threading
import string
import time
import sys
import numpy as np
import pyfiglet

class colors:
    red = '\033[31m'
    green = '\033[32m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

def credits():
    credits = pyfiglet.figlet_format("H  e  l  l  o")
    print(f'{colors.red}Made by' + credits)
credits()

animation_finished = False

def animation():
    for x in itertools.cycle(['|', '/', '-', '\\']):
        if animation_finished:
            break
        sys.stdout.write('\rLoading NitroGen ' + x)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animation)
t.start()
time.sleep(5)
animation_finished = True


codes_needed = input(f'\n{colors.lightcyan}Do you want to see the chance of getting a nitro code[Y/N]')
if codes_needed == 'Y':
    x = 100000,200000,300000,400000
    y = 2,3,4,6
    plt.plot(x,y)
    plt.xlabel('NitroCodes you want to generate')
    plt.ylabel('Nitrocodes you will get')
    plt.show()


gens = int(input(np.array((f'{colors.pink}\nInput How Many Codes to Generate and Check: '))))
print('---------------------------------------------------------------------------------------')

with open("NitroCodes.txt", "w", encoding='utf-8') as file:
    print(np.array('Nitrocodes are being generated'))
    time.sleep(2)
    for i in range(gens):
        code = np.array("".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16)))

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        request = requests.get(url)

        if request.status_code == 200:
            print(np.array(f"{colors.green} NITRO-CODE-FOUND : \n{nitro} "))
            break
        else:
            print(np.array(f"{colors.red} Not-Working : \n{nitro} "))





