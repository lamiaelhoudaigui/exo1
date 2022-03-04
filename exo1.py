
def syrac(n):
 
    listsyrac=list()
    if (type(n) != type(1) or n<1):
        return None 
 
    while n!=1:
        if n%2 == 0:
            n=n/2
        else:
          n=(n*3)+1
        print(n)


syrac(int(input()))