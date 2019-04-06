
def Star():
    n=int(input('Enter the length of the pattern'))
                   
    
    for i in range (n,0,-1):
        
        print(i*'+' + ((n-i)*2) * ' ' + i * '+')
        
        
    for i in range (n):
        print(i * '+' + ((n-i)*2)* ' ' + i* '+') 

  

       
Star()
       
    
