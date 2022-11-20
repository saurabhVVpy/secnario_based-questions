#1
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[10,20,30,40,50]

if len(l1)==max(len(l1),len(l2)):
    key_=l1
    value_=l2
else:
    key_=l2
    value_=l1

res={}

for k in range(len(key_)):
    try:
        res[ key_[k] ] = value_[k]
    except:
        res[ key_[k] ]=0 #set default value to something here i took zero    

print(res)

#2
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[10,20,30,40,50]

if len(l1)==max(len(l1),len(l2)):
    key_=l1
    value_=l2
else:
    key_=l2
    value_=l1

res={key_[i]:value_[i] if i<len(value_) else 0 for i in range(len(key_)) }
print(res)

#3

l1=[1,2,3,4,5,6,7,8,9,10]
l2=[10,20,30,40,50]

if len(l1)==max(len(l1),len(l2)):
    key_=l1
    value_=l2
else:
    key_=l2
    value_=l1

res=dict([(key_[i],value_[i]) if i<len(value_) else (key_[i],0) for i in range(len(key_))])
print(res)