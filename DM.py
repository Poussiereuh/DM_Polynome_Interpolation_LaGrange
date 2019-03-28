from sympy import *

liste_valeurs_entrees = [-0.5, 0, 0.25, 1]
liste_f_x_result = []
liste_L = []

#On défini i
nbr_valeurs = 3 #input("i vaut: ")
valeur_n = 3 #input("n vaut: ")

#On récupère chaque xi puis on calcul f(xi)
for i in range(0, int(nbr_valeurs)+1):
    #liste_valeurs_entrees.append(float(input("i{} vaut: ".format(val))))
    liste_f_x_result.append(2*liste_valeurs_entrees[i]/(liste_valeurs_entrees[i]+1))

for n in range(0, int(valeur_n)+1):
    L_x_h = ''
    L_x_b = ''
    for i in range(0, int(valeur_n)+1):
        if i == n:
            pass
        else:
            L_x_h += "(x - {})".format(liste_valeurs_entrees[i])
            L_x_b += "({} - {})".format(liste_valeurs_entrees[n], liste_valeurs_entrees[i])

    liste_L.append("L{}(x) = {}/{}".format(n, L_x_h, L_x_b))
    print("L{}(x) = {}/{}".format(n, L_x_h, L_x_b))

print(liste_valeurs_entrees)
print(liste_f_x_result)
print(liste_L)

polynome = ''

for l in range(0, int(nbr_valeurs)+1):
    polynome += "{} * {}"
