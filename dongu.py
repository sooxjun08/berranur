t=1
while t<=5:
    
    while True :
        e=input("birinci notun ne ")
        if e.isdigit()==True and 0<=int(e)<=100:
            e=int(e)
            break
        else:
            print("sayı giriniz ")
        
        
        
    while True :
        i=input("ikinci ")
        if i.isdigit()==True and 0<=int(i)<=100:
            i=int(i)
            break
        else:
            print("sayı giriniz")
            
        
    ort=(e+i)/2
    print(ort)
    t+=1 #t=t+1