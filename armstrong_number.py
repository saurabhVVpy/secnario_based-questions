# armstrong number
# 1

def arm_strong():
    try:
        number=int(input('Enter number:'))
        power=len(str(number))
        result=0
    
        for num in str(number):
            result=result+(int(num)**power)

        if result==number:
            return 'Palindrome'
    
        else:
            return 'Not Palindrome'


    except:
        print('******Enter Valid number********')
        return arm_strong()
    
    
print(arm_strong())


# 2

def arm_strong():
    try:
        number=int(input('Enter number:'))
        result=sum([int(num) ** len(str(number)) for num in str(number)])
    
        if result==number:
            return 'Palindrome'
    
        else:
            return 'Not Palindrome'
        
    except:
        print('*********Enter Valid number********')
        return arm_strong()
    
print(arm_strong())