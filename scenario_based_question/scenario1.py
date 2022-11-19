st1 = 'brain$work&'
# st1 = "123$456%7489*0^"

ls = list(filter(lambda x: x if x.isalnum() else False, st1))[::-1]

j = 0
for i in st1:
    if not i.isalnum():
        ls.insert(j, i)
    j += 1
result = ''.join(ls)
print(result)
