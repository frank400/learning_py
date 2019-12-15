from math import sqrt
D=input("enter a list of numbers in a comma-sepparated: ")
C=50
H=30
Inicial_list=D.split(',')
interlist=[int(Inicial_list[i]) for i in range(len(Inicial_list))]
Final_list=[sqrt((C*2*N)/H)for N in interlist]
print(Final_list)
