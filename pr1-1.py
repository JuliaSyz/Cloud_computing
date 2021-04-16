def fun(array, k=0, sum=0):
    if k < len(array):
        sum += fun(array, k+1, array[k])
    return sum

mass = list(map(int,input().split()))
print(fun(mass))