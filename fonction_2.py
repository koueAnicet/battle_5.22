

def nombre_first(b=int(input('nombre:'))):
    
    nb_premier =[]
    list_nb_comp=[]
    
    for num in range(2, 100+1):
        prime = True
        for i in range(2, num):
            if num%i== 0:
                prime = False
        if prime:
            nb_premier.append(num)

    for i in range(2,b):
            if b%i == 0:
                return False
    for y in range(i):
        if y in nb_premier:
            list_nb_comp.append(y)
    return f'\nC\'est un nombre premier, la liste des nombre compris entre {b} est: \n{list_nb_comp}.\n'
        
print(nombre_first())

# def is_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True   
# print(is_prime(77))