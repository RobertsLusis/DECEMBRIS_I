#Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.

ievade=int(input("Ievadiet skaitli:"))

if ievade%2==0:
    print("SKaitlis ir pāra.")
else:
    print("Skaitlis ir nepāra.")