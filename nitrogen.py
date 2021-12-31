import requests
import random
import threading
import string
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import itertools
import pyfiglet as pf

done = False


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading Simulation ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()

# long process here
time.sleep(5)
done = True
class colors:
    red = '\033[31m'
    green = '\033[32m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

def credits():
    credit = pf.figlet_format("H  e  l  l  o")
    print(f'{colors.red}\nMade by' + credit)
credits()
codes_needed = input(f'\n{colors.lightcyan}Do you want to see the chance of getting a nitro code[Y/N]')
if codes_needed == 'Y':
    x = 100000,200000,300000,400000
    y = 2,3,4,6
    plt.plot(x,y)
    plt.xlabel('NitroCodes you want to generate')
    plt.ylabel('Nitrocodes you will get')
    plt.show()

gens = int(input('Input How Many Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print(f"{colors.green}NitroCodes are being generated")



    for i in range(gens):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,k = 16))



        file.write(f"https://discord.gift/{code}\n")



with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        request = requests.get(url)

        if request.status_code == 200:
            print(np.array(f" {colors.green}\nValid | {nitro} "))
            break
        else:
            print(np.array(f" {colors.red}\nNot-Working | {nitro} "))


