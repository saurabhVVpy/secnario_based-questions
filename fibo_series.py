

#Saurabh's

def fibo_series():
    try:
        length = int(input('Tell the length of series: '))
    except:
        print("*************Enter Valid Number****************** ")
        fibo_series()

    initials = [0, 1]
    result = '0 1'

    for i in range(length - 2):
        result = result + ' ' + str(sum(initials))
        initials = [initials[1], sum(initials)]
    return result


print(fibo_series())


# code changes by prathamesh
def fib_number():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Aniruddha

n = int(input("Enter the numbers of element : "))
a = int(input("Enter the first number: "))
b = int(input("Enter the Second number: "))
print(a, b, end=" ")
while n-2:
    c = a + b
    a = b
    b = c
    print(c, end=" ")
    n -= 1

ans = fib_number()

for i in ans:
    if i > 100:
        break
    print(i)


###------------------------------ Add Factorial numbers---------------------------#
fact=(lambda num:1 if num==0 else num*fact(num-1) )
print(fact(5))