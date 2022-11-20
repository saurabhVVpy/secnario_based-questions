#1
######## using reverse method #########

l=[1,2,3,4,5,6,7]
l.reverse()
print(l)

#2
########## using reversed method ###########
#reversed returns iterable object
l=[1,2,3,4,5,6,7]
# l=list('saurabh')
res_=[x for x in reversed(l)]
# res_=list(filter(lambda x:x ,reversed(l)))
# res_=list(map(lambda x:x*1 ,reversed(l)))
print(res_)


#3
###### using slicing method ########
l=[1,2,3,4,5,6,7]
l=l[-1::-1]
print(l)

#4
###### using insert method ########
l=[1,2,3,4,5,6,7]
res_=[]
for i in l:
    res_.insert(0,i)
print(res_)