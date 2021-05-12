#using Nilakantha's Series

def pi():
    val = 0
    for i in range(1,1000000+1):
        num = 2*i
        val = val + ((pow(-1,i)*4*-1)/(num*(num+1)*(num+2)))
    return val+3

print(pi())