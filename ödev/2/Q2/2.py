

def deger():
    global a,b
    a=[]
    b=[]
    while True:
        x=input("")
        if x=="END":
            y=input("")
            b=b+y.split("-")
            break
        else:
            a=a+x.split(":")

def dic(n):
    global kume
    kume={}
    for i in range(len(n)):
        if i%2==0:
            kume[n[i]]=n[i+1]
            
            
def son(n1,n2):
    a=0
    if n2[0] in n1[n2[1]]:
        print("True")
    elif n2[0]==n2[1]:
        print("True")
    else:
        print("False")
    
    

deger()
dic(a)
son(kume,b)

