def hcf(a,b):
    
    '''Please enter bigger number at first'''
    
    if b == 0:
        return a
    else:
        return hcf(b, a % b)
print(hcf.__doc__)
print(hcf(65, 25))      # 5