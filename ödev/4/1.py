def yaso(a):
    global q
    if int(a[2])+1<10:
        q=(a[0]+"-"+a[1]+"-"+str(0)+str(int(a[2])+1))
    else:
        q=(a[0]+"-"+a[1]+"-"+str(int(a[2])+1))


def fis(a,b):
    global c1
    c1=[]
    a2=0
    while a2<=(int(b[1])-int(a[1])):
        a1=1
        if int(a[1])+a2==int(b[1]):
            while a1<=int(b[2]):
                if a1==int(b[2])+1 and int(a[1])+a2==int(b[1]) :
                    break
                elif int(a[1])+a2==int(a[1]) and a1<int(a[2]):
                    a1=a1+1
                else:
                    if a1<10:
                        if int(a[1])+a2<10:
                            c1.append(a[0]+"-"+str(0)+str(int(a[1])+a2)+"-"+str(0)+str(a1))
                            a1=a1+1
                        else:
                            c1.append(a[0]+"-"+str(int(a[1])+a2)+"-"+str(0)+str(a1))
                            a1=a1+1
                    else:
                        if int(a[1])+a2<10:
                            c1.append(a[0]+"-"+str(0)+str(int(a[1])+a2)+"-"+str(a1))
                            a1=a1+1
                        else:
                            c1.append(a[0]+"-"+str(int(a[1])+a2)+"-"+str(a1))
                            a1=a1+1
        else:
            while a1<=31:
                if a1==int(b[2])+1 and int(a[1])+a2==int(b[1]):
                    break
                elif int(a[1])+a2==int(a[1]) and a1<int(a[2]):
                    a1=a1+1
                else:
                    if a1<10:
                        if int(a[1])+a2<10:
                            c1.append(a[0]+"-"+str(0)+str(int(a[1])+a2)+"-"+str(0)+str(a1))
                            a1=a1+1
                        else:
                            c1.append(a[0]+"-"+str(int(a[1])+a2)+"-"+str(0)+str(a1))
                            a1=a1+1
                    else:
                        if int(a[1])+a2<10:
                            c1.append(a[0]+"-"+str(0)+str(int(a[1])+a2)+"-"+str(a1))
                            a1=a1+1
                        else:
                            c1.append(a[0]+"-"+str(int(a[1])+a2)+"-"+str(a1))
                            a1=a1+1
        a2=a2+1
                
dosya=open("time-series-19-covid-combined.csv","r")
x=input("")
y1=input("")
y2=input("")
a1=y1.split("-")
a2=y2.split("-")
fis(a1,a2)
yaso(a2)



print("index	confirmed	recovered	deaths")
f=0
while True:
    z=dosya.readline()
    d=z.split(",")
    if x in z:
        for i in range(len(c1)+1):
            if i<len(c1) and c1[i] in z:
                f=f+1
                azra=str(f)+"\t"+str(d[3])+"\t"+str(d[4])+"\t"+str(d[5])
                print(azra,end="")
    else:
        if d[1]!="Country/Region":
            if str(d[1])>str(x):
                break 
     

            
        

         
        
    
        
            
    
    
