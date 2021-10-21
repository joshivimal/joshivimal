def HCF(a,b):
    if a == 0:
        return b
    return HCF(b % a, a)
def lcm(a,b):
    return (a / HCF(a,b))* b
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))
print('HCF of', a, 'and', b, 'is', HCF(a, b))