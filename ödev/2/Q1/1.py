a=[]
xo=[]
def deger(n1,n2):
    if len(n2[n1])==1:
        xo.append(n2[n1])
    else:
        a.append(str(n2[n1]))
def karsi(n):
    global f
    n.sort()
    if len(n)>0:
        f="'"+"0"+" | "+(" ").join(n)+"' "
    else:
        f=""
z={}
z1=[]

def ayni(n):
    x=[]
    for i in n:
        for j in n:
            if (i)[0]==(j)[0]:
                x.append(str(j)[1])
        sorted(x)
        z[(i)[0]]=(" ").join(x)
        if str(i)[0] not in z1:
            z1.append(str(i)[0])
        x=[]

        
def son(n,a):
    global f1
    f1=""
    n.sort()
    for i in range(len(n)):
        if i==len(n)-1:
            f1=f1+"'"+n[i]+" | "+a[n[i]]+"'"
    
        else:
            f1=f1+"'"+n[i]+" | "+a[n[i]]+"' "
                
                
            
#listedeki eleman sayısını ve elemanları kullanıcıdan alır
        
def girdi():
    global eleman_s,eleman
    eleman_s=int(input(""))
    x=(input(""))
    eleman=x.split(" ")
        

girdi()
for i in range(eleman_s):
    deger(i,eleman)
karsi(xo)
ayni(a)
son(z1,z)
print(f+f1)
