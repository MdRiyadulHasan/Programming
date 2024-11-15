def isUgly(n: int) -> bool:
    if n<=0:
        return False
    for factor in [2,3,5]:
        while n%factor==0:
            n//=factor
    return n==1
n = 6
isUgly(n)