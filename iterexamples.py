list1=[12,3,4,55,43]
list2=iter(list1)
next(list2)

ages=[5,12,17,18,24,32]

for a in ages:
    if a >=18:
        print(a)

#filter
def fltr(a):
    if a <18:
        return True  
    else:
        return False
list(filter(fltr,ages))          

#numerical data type

import numpy as np
list1=[1,2,3,4,5,6,7,8]
ar=np.array(list1)
ar
type(ar)
dir(ar)
ar.sum()

#0 dimension array
ar1=np.array(12)
ar1.shape
#1d
ar2=np.array([1,2,3,4])
ar2
ar2.shape
ar2.size
#2d
list1=[[1,2,3,4,5],[6,7,8,9,10]]
ar3=np.array(list1)
ar3
ar3.shape

list2=[[[1,2,3,4,5],[6,7,8,9,10]],[[1,2,3,4,5],[6,7,8,9,10]]]
ar4=np.array(list2)
ar4
ar4.shape
#3d
list3=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
ar3=np.array(list3)
ar3
ar3.shape

#reshape
list3=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
ar3=np.array(list3)
ar3
ar3.shape
reshape1=ar3.reshape(5,3)
reshape1
#row selection
reshape1[0]
reshape1[1]
#coloum selection
reshape1[:,0]
reshape1[:,1]
#row and coloum selection
reshape1[1,2]
reshape1[0:2,0]
reshape1[2:4,1]
reshape1[2:4,0:3:2]
#arange function
list(range(5,17,2))#list data
np.arange(5,17,step=2)#array data

#zeros ones
np.zeros(3)
np.zeros([3,3,3])
np.ones(3)
np.ones([3,3,3])
#ones multi numbers
np.ones([2,3,3])*5

#linspace divides
np.linspace(0,100,5)
