print("\n*****THEOREME*******\n")

hypo= int(input("Donnez l'hypothenus:\t"))
c1= int(input('donnez un coté: \t'))
from math import sqrt
def pythagore(c1,hypo):

    if c1 and hypo:
        
        x = int(sqrt(hypo**2 - c1**2))
        
        if hypo**2 == c1**2 + x**2:
            print("\n #---C'est un triangle retangle---#")
            return f"Le coté est : {x}."
        return "C'est pas un triangle retangle\n"
        
print("\n",pythagore(c1,hypo))
