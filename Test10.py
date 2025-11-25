numbers = [2,1,0,4,8,6,9,3,10,5,7]

list1=[]
def check_prime(n):
    count = 0
    for i in range(2,n):
        if (n%i==0):
            count+=1
    if (count == 1):
        return n

