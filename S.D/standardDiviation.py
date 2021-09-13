import math
##data=[60,61,65,63,98,99,90,95,91,96]
data = [20,69,56,90,40,99,86,100,70,69,80,65,57,82,90,70,79,39,90,80,86,53,97,95,88,47,100,56,97,100]

def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean
squaredList=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squaredList.append(a)
sum=0
for i in squaredList:
    sum=sum+int(i) 
n=len(data)    
result=sum/n-1          
standardDeviation=math.sqrt(result)
print(standardDeviation)