def power(base, pow):
    res = 1
    for index in range(pow):
        res = res*base
    return res
    
print(power(2,8))
        