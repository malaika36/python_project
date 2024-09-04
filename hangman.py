import random
li = ["apple","banana","shake","karbon","charcoal","pakistan","momina","anaconda"]
ran = random.choice(li)
dis = []
l = 6
for i in range(len(ran)):
    dis.append('-')
gm = False
while not gm:
    g = input("guess the word: ")
    for i in range(len(ran)):
        if(g==ran[i]):
            dis[i]=g
    print(dis)
    if g not in ran:
            l = l -  1
            if l==0:
               print("you lose")
               gm = True
    if '-' not in dis:
        print("congratulation")
        gm =True
print("game over")
    
    
    
    
    

    
    