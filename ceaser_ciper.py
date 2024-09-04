def encrypt(k ,l,b):
    res = []
    for char in range(ord('a'), ord('z') + 1):
        res.append(chr(char))
        nes = ""
    for i in l:
       s = res.index(i)
       new = (s+b)%26 
       nes = nes + res[new]
    print(nes)
def decrypt(k,l,b):
    res = []
    for char in range(ord('a'), ord('z') + 1):
        res.append(chr(char))
        nes = ""
    for i in l:
       s = res.index(i)
       new = (s-b)%26
       if(new<=0):
           new = new + 26
       else: 
           nes = nes + res[new]
    print(nes)
ans = "yes"
while ans=="yes":
    k  = input("enter the e for encryption or d for dycryption: ")
    s = int(input("enter the shift key: "))
    w = input("enter the word: ")
    if(k=="e"):
        encrypt(k,w,s)
    elif(k=="d"):
        decrypt(k,w,s)
    elif (ans=="no"):
        ans == "no"
    ans = input("do you want to repeat yes or no: ")
print("goodbye")
