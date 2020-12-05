import numpy as np

#to created an array
a=np.array([[1,2,3],[4,5,6],[8,9,10]])
#to check the Data type of array
print("Data Type of Array:",a.dtype)

print("2D Array:",a)
#To create an array with start, end value with particular limit

arng=np.arange(1,9,2)
print("Arange Array:",arng)


#linspace of numpy used to create an array with particular count in given range
lin=np.linspace(1,11,20)
print("linspace Array:",lin)

#to create a zero matric with given dimensions
ze=np.zeros((3,3),float)
print("zero matrix with data type\n:",ze)

#to check the shape of array
print("shape of the array:",ze.shape)

# Reshape the array
resh=np.random.random((3,3))
print("original Array:\n",resh)
print("Reshaped array:\n",resh.reshape(3,3))

#to Create a unique Matrix

print(np.full((3,3),1))


#Compare the two arrays 
print(np.equal(a,resh))
#compare Whole array
print(np.array_equal(a,resh))

#Array Broadcasting
#a1=np.array([[1,2,3],[4,5,6],[7,8,9]])#np.random.randomint((3,3))
#a2=np.array([[1,2,3]])#np.random.randomint((1,3))
#print(np.sum([a1,ze]),axis=0)






