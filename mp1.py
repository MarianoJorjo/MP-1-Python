import matplotlib.pyplot as plt
n = 0
valuees = []
while n <= 99:
    x = n
    if x >= 10:
        while x >= 10:
           z = x - 10
           x = z
          
    if x <= 9:
        y = x**2 - 7
        print(y)
        valuees.append(y)
    n = n+1
print(valuees)
plt.xlim(None,100)
plt.stem(valuees,use_line_collection=True)
plt.show()


    
    
    
    
    
        
