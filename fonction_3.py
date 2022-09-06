



def tab_nombre(v)->list:
    nbNeg,nbPos =[],[]
    nb =0
    resulSomNbre=0
    nb = int(input("Entrez 5 nombre: \t"))
    v.append(nb)

    i = 1
    while len(v) < 5:
        i +=1
        nb = int(input(f"\nEntrez le {i}ème nombres: \t"))
        v.append(nb)
        if nb < 0:
            nbNeg.append(nb)
        else:
            nbPos.append(nb)
        
    
    resulSomNbre = sum(nbPos) + sum(nbNeg)
    
    print(f"\nLa somme des positif: {sum(nbPos)} \nLa somme des negatifs: {sum(nbNeg)}\n")
    if resulSomNbre :
        if resulSomNbre  > 0:
            return 'Restulta: Positif'
        elif resulSomNbre < 0: 
            return 'Restulta: Négatif'
        elif resulSomNbre == 0 :
            return "Restulta: égaux"
        return "-1" 
print(tab_nombre(v=[]))