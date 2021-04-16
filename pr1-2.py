def fun(array, k=0, dict={}):
    if k < len(array):
        if array[k][0] not in dict.keys():
            dict[array[k][0]] = len(array[k])
        else:
            if dict.get(array[k][0]) < len(array[k]):
                dict[array[k][0]] = len(array[k])
        fun(array, k+1, dict)
    return [[key,v] for key,v in dict.items()]


mass = list(map(str,input().split(' ')))
print(fun(mass))