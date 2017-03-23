#waiting on learning threading. trying to solve simple voltage divider problem 

inputV = 12
outV = 5

current = 2.5 

#to achieve the above with a voltage divider, (2R in series), Z1 + Z2 needs to be 4.8

sumOfimpedance = inputV/current

#print(sumOfimpedance)

#now to search for a convergence
Z1 = []
Z2 = []
Sums = []

for i in range(0,5):
	tempZ1 = i
	tempZ2 = 5/7.0*tempZ1
	Z1.append(tempZ1)
	Z2.append(tempZ2)
	Sums.append(tempZ1+tempZ2)
print (Z1)
print (Z2)
print(Sums)