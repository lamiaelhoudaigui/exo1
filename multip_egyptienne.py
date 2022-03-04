
def mult_egyptienne(a,b):

        resultat=0

        while a!=0:

            if a%2==1:

                resultat+=a

            a>>=1

            b=b+b

        return resultat



var = mult_egyptienne(2,3)

print(var)