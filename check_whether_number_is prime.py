def check_prime():
    try:
        number_=int(input('Enter num: '))
    except:
        return check_prime()

    if number_<=1:
        return 'Number should be greater than 1'
    
    elif number_==2:
        return 'Prime'
    
    else:
        if all([ number_ % num!=0 for num in range(2,int(number_**0.5)+1)]):
            return 'Prime'
        else:
            return 'Not prime'

print(check_prime())