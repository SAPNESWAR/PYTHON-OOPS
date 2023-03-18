'''
#List Comprehension

#for loop version
result=[]
for i in range(11):
    result.append(i)
print(result)
'''


"""
#list comprehension
print([i for i in range(11)])

#for loop version --> odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)


print([i if i%2!=0 else i**2 for i in range(11)])
"""

#for loop --odd-->square it
#even-->cube it
"""
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for i in range (len(mat)):
    for j in mat[i]:
        if j%2!=0:
            result.append(j**2)
        else:
            result.append(j**3)
print(result)
print([j**2 if j%2!=0 else j**3 for i in range(len(mat)) for j in mat[i]]) """



'''
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result=[]
for row in mat:
    row_data=[]
    for ele in row:
        
        if ele%2!=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result.append(row_data)
print(result)


#List Comprehension
print([ele**2 if ele%2!=0 else ele**3 for row in mat for ele in row])
print([[ele**2 if ele%2!=0 else ele**3 for ele in row] for row in mat])
'''
#-------------------------------------------------------------------------

#Paired Outputs
#(problem Statement:For each number in list_b,get the number and its position(index)
#in mylist as are turn list of tuples)
#mylist=[9,3,6,1,5,0,8,2,4,7]
#list_b=[6,4,6,1,2,2]
#result=[(6,2),(4,8)]

mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[]

for i in list_b:
    result.append((i,mylist.index(i)))
print(result)

print([(i,mylist.index(i)) for i in list_b])





































