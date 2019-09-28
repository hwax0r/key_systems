def euclid_simple(a, b):
    if b == 0:
        print(a)
    else:
        euclid_simple( b , a % b )
euclid_simple(1071, 462) # 21

def euclid(a,b):
    if b == 0:
        print(a)
    else:
        while (b)!= 0:
            c = b
            b = a % b
            a = c
        print(a)
euclid(1071, 462) # 21
