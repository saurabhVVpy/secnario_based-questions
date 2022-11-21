#print digits in list of tuples
#for variable length of tuple

input=[(1,23),(72,3),(8,10),(18,3),(7,8)]
res=set()
{res.update(str(num)) for tup in input for num in tup}
res=sorted(res)
print(','.join(res))

#for tuple with exact two elements
input=[(1,23),(72,3),(8,10),(18,3),(7,8)]
res=set()
{res.update(str(i[0])+str(i[1])) for i in input}
res=sorted(res)
print(','.join(res))

#
input=[(1,23),(72,3),(8,10),(18,3),(7,8)]
res=set()
{res.update(str(k)+str(v)) for k,v in dict(input).items()}
res=sorted(res)
print(','.join(res))







