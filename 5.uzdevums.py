#Izveidojiet Python programmu,
#kas atkarībā no pašreizējās stundas
#izvada atbilstošu sveicienu, izmantojot if priekšrakstu. (labrīt, labdien, labvakar)

import datetime
from time import time 

def noteikt_laiku(laiks):
    if datetime.time<=00 and datetime.time>12:
        print("labrīt")
    elif datetime.time<=12 and datetime.time>17:
        print("labdien")
    elif datetime.time<=17 and datetime.time>00:
        print("labvakar")