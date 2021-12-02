#19 dakika 46 saniye-19 Ocak 2021
def filiz():
    z=input("")
    j=""
    i=0
    while i<len(z):
        if z[i]=="[":
            j=j+z[i]
            a=i+1
            f=1
            while a<len(z):
                if z[a]=="[":
                    j=j+z[a]
                    a=a+1
                    f=f+1
                elif z[a]=="]":
                    j=j+z[a]
                    f=f-1
                    a=a+1
                if f==0:
                    print(j,end=" ")
                    j=""
                    i=a
                    
filiz()
                    
                    
            
            
