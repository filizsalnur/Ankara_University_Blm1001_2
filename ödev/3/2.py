def girdi():
    global ilk,b
    ilk=[]
    b=[]
    while True:
        x=input("")
        if x=="END":
            y=input("")
            b=b+y.split("-")
            break
        else:
            ilk=ilk+x.split(":")

def dic(n):
    global kume
    kume={}
    for i in range(len(n)):
        if i%2==0:
            kume[n[i]]=n[i+1]
            
def dic2(n,a):
    global kume2
    kume2={}
    for j in range(len(a)):
        if j%2==0:
            f=""
            f=f+a[j]+n[a[j]]
            b=a[j]
            z=a[j+1].split(",")
            for l in z:
                for g in range(len(a)):
                    if g%2==0:
                        if l==a[g]:
                            f=f+","+n[l]
            kume2[b]=f
            f=""                

def dic3(n,a):
    global kume3
    kume3={}
    for j in range(len(a)):
        if j%2==0:
            f=""
            f=f+n[a[j]]
            b=a[j]
            z=a[j+1].split(",")
            for l in z:
                for g in range(len(a)):
                    m1=n[b].split(",")
                    if g%2==0:
                        if l==a[g]:
                            m2=n[l].split(",")
                            for g2 in m2:
                                if g2 not in m1:
                                    f=f+","+g2
            kume3[b]=f
            f=""          
  
            
def karsi(n,a,a2):
    for i in range(len(a2)):
        min=100
        if i%2==0:
            if a[0] in n[a2[i]] and a[1] in n[a2[i]]:
                if len(n[a2[i]])<min:
                    min=len(n[a2[i]])
                    f=a2[i]
    print(f)
                
    

        
girdi()
dic(ilk)
dic2(kume,ilk)
dic3(kume2,ilk)
c=0
while c<len(ilk)/2:
    dic3(kume3,ilk)
    c=c+1

karsi(kume3,b,ilk)

