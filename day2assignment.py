#creating a list 
lst1=[1,2,6,7,9,3,4]
lst=[] #creating an empty list
for i in lst1: #takes the each value from a list
	if(i%2==0):  #checks the if condition for each iteration
		lst.append(i) 
print(f"The even numbers from a given list is {lst}")
	