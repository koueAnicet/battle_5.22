

def nombre_first(b=input('nombre:'))->int:
    v =[5]
    
    for i in range(b):
        if i % b == 1 and i % 1 == b:
            print(i)
      
        
print(nombre_first(5))