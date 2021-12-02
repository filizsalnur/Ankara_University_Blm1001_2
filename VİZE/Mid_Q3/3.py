#25 dakika-19 Ocak 2021
def filiz():
    import math
    x=0
    y=0
    z=""
    while z!="-1":
        z=input("")
        a=z.split(" ")
        try:
            if a[0]=="left":
                x=x+int(a[1])
            if a[0]=="right":
                x=x-int(a[1])
            if a[0]=="up":
                y=y+int(a[1])
            if a[0]=="down":
                y=y-int(a[1])
            if "left" not in a and "right" not in a and "up" not in a and "down" not in a and "-1" not in a:
                dire
           
        except:
            print("invalid")
    o=x**2+y**2
    u=math.sqrt(o)
    
    print("dist",":",float(u))
        
        






filiz()
