import random

while True:
    save = input("Wanna Save Code In A Txt File (y/n): ")
    if save == "y" or save == "n":
        break
    else:
        print("Enter Valid Choice")
choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
               "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","~","`","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","'","{","}","/","|",",","<",">",".","?",";",":"]

numba = 0
limit = int(1)
numba1 = random.choice(choices)
numba2 = random.choice(choices)
numba3 = random.choice(choices)
numba4 = random.choice(choices)
numba5 = random.choice(choices)
numba6 = random.choice(choices)
numba7 = random.choice(choices)
numba8 = random.choice(choices)
numba9 = random.choice(choices)
numba10 = random.choice(choices)
numba11 = random.choice(choices)
numba12 = random.choice(choices)
numba13 = random.choice(choices)
numba14 = random.choice(choices)
numba15 = random.choice(choices)
numba16 = random.choice(choices)
numba17 = random.choice(choices)
numba18 = random.choice(choices)
numba19 = random.choice(choices)
numba20 = random.choice(choices)
numba21 = random.choice(choices)
numba22 = random.choice(choices)
numba23 = random.choice(choices)
numba24 = random.choice(choices)
numba25 = random.choice(choices)
numba26 = random.choice(choices)
numba27 = random.choice(choices)
numba28 = random.choice(choices)
numba29 = random.choice(choices)
numba30 = random.choice(choices)
numba31 = random.choice(choices)
numba32 = random.choice(choices)
numba33 = random.choice(choices)
numba34 = random.choice(choices)
numba35 = random.choice(choices)
numba36 = random.choice(choices)
numba37 = random.choice(choices)
numba38 = random.choice(choices)
numba39 = random.choice(choices)
numba40 = random.choice(choices)

code_save = f"{numba1}{numba2}{numba3}{numba4}{numba5}{numba6}{numba7}{numba8}{numba9}{numba10}{numba11}{numba12}{numba13}{numba14}{numba15}{numba16}{numba17}{numba18}{numba19}{numba20}{numba21}{numba22}{numba23}{numba24}{numba25}{numba26}{numba27}{numba28}{numba29}{numba30}{numba31}{numba32}{numba33}{numba34}{numba35}{numba36}{numba37}{numba38}{numba39}{numba40}"
print(
        f"{numba1}{numba2}{numba3}{numba4}{numba5}{numba6}{numba7}{numba8}{numba9}{numba10}{numba11}{numba12}{numba13}{numba14}{numba15}{numba16}{numba17}{numba18}{numba19}{numba20}{numba21}{numba22}{numba23}{numba24}{numba25}{numba26}{numba27}{numba28}{numba29}{numba30}{numba31}{numba32}{numba33}{numba34}{numba35}{numba36}{numba37}{numba38}{numba39}{numba40}")
numba = int(numba) + 1
if numba == limit:
    print("Done")

if save == "y":
    the_file = open("Password.txt", "a")
    the_file.write(f"{str(code_save)}\n")
    the_file.close()
input()
