# Autokey cipher:

def encrypt():
    pt=str(input("enter plain text "))
    key=int(input("enter your key "))
    p=[]
    ct=""
    j=0
    for i in range(len(pt)):
        y=ord(pt[i])-ord("a")
        p.append(y)
        if(i==0):
            z=key+y%26
        
            if(z<0):
                z=z+26
            elif(z>=26):
                z=z-26
            #print(y,key,z)
            ct+=chr(z+ord("a"))
        else:
            key=p[j]
            z=key+y%26
        
            if(z<0):
                z=z+26
            elif(z>=26):
                z=z-26
            #print(y,key,z)
            ct+=chr(z+ord("a"))
            j+=1
        #print(p)
    print(ct)

def decrypt():   
    ct=str(input("enter cipher text "))
    key=int(input("enter your key "))
    p=[]
    pt=""
    j=0
    for i in range(len(ct)):
        y=ord(ct[i])-ord("a")
    #p.append(y)
        if(i==0):
            z=(y-key)%26
        
            if(z<0):
                z=z+26
            elif(z>=26):
                z=z-26
            
            p.append(z)
            pt+=chr(z+ord("a"))
        else:
            key=p[j]
            z=(y-key)%26
        
            if(z<0):
                z=z+26
            elif(z>=26):
                z=z-26
            
            p.append(z)
            pt+=chr(z+ord("a"))
            j+=1
        
    print(pt)  

print("1. Encryption: \n2. Decryption:\n")
r=int(input("enter your choice\n ==> "))
if(r==1):
    encrypt()
elif(r==2):
    decrypt()
else:
    print("Invalid choice")
    