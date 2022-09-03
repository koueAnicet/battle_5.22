print("*****THEOREME*******\n")


def pythagore(c1,c2):

    if c1 and c2:
        
        c3= (c2**2 + c1**2)**(1/2)
        return 'le coté est :' , int(c3)
        
print(pythagore(2,4))
