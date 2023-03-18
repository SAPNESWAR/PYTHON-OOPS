'''
s1=input().replace(" ",'')
s2=input().replace(" ",'')
a=[]
b=[]
c=[]
for i in s1:
    a.append(i)
for i in s2:
    b.append(i)
for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])
d=''
for i in c:
    d+=i
print(d)
'''
s1=input()
s2=input()
ans=""
for i in s1:
    if i==" ":
        continue
    for j in s2:
        if(i==j and j not in ans):
            ans+=i
print(ans)
