def euclidGcd(a,b):
    if a%b==0:
        return b
    return euclidGcd(b,a%b)


def euclidLcm(a,b):
    return (a*b)/euclidGcd(a,b)

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def findSumOfMultiples(a,b,target):
    sum=0
    lcm=euclidLcm(a,b)
    a1=target/a
    b1=target/b
    if(target%a==0):
        a1=a1-1
    if(target%b==0):
        b1=b1-1
    for i in range(a1):
        sum=sum+(a*(i+1))

    for j in range(b1):
        val=b*(j+1)
        if not val%lcm==0:
            sum=sum+val
    return sum;

print findSumOfMultiples(3,5,1000)


