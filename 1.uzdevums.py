#Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.

skaitlis =int(input("Ievadi skaitli:"))

summa=0

for skaitit in range(1, skaitlis+1):
    summa+=skaitit

print("Skaitļu summa no 1 līdz tavam izvēlētajam skaitlim ir:", summa)