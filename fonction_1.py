print("*****THEOREME*******\n")

c1= int(input('nombre1:\t'))
c2= int(input('nombre2: \t'))

def pythagore(c1,c2):

    if c1  and c2 :
        c3 =c2**2 + c1**2 
        
        n= (c2**2 + c1**2)**(1/2)
        if c3**2 == n:
            return 'le coté est :' , int(c3)
        return "cest pas un triangle retangle\n"
        
print("\n",pythagore(c1,c2))
