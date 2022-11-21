def prime():
    try:
        number_=int(input('Enter num: '))
    except:
        return prime()
    
    prime_num=[]    
    
    for num in range(number_+1):
       
        if number_<=1:
            return 'number should be greater than 1 '
            
        elif number_==2:
            return 2
            
        elif num>=2:
            if all([ num % i != 0 for i in range(2,int(num**0.5)+1) ]):
                prime_num.append(num)
            
    return prime_num    

print(prime())
