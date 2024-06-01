#Genetic Algorithm
import random
from time import time
start=time()
word=input("please enter the word/phrase you would like the program to find") # used to create a 'similarity score'
wordlen=len(word) #used to create a 'length score'
maxscore=wordlen+1
maincomparison = []#add word and word length to debug ["t","w","a","t",4]
dataset =127  #127 makes it faster, 1114111 makes it more exhaustative
#first genetic cycle
for j in range (1,11):
    comparison = []
    loopone=wordlen #To unleash pure chaos, make this number infinite
    for i in range(loopone):
        #ascii charater codes to letters
        x=random.randint(0,dataset) 
        z=chr(x)
        comparison.append(z)
    comparison.append(loopone)
    maincomparison.append(comparison)
tots=[]
for k in maincomparison:
    score=0
    runner=0
    #length scores
    if k[-1] == wordlen:
        score+=1
    #character confirmation
    try:
        for l in word:
            if k[runner] == word[runner]:
                score+=1
                runner+=1
            else:
                runner+=1
    except:
        IndexError
    k.append(score)
    tots.append(k)
#weighting comparisons
bigtots=sorted(tots,key=lambda change:change[-1], reverse=True)
#actual genetic loop
carry1=bigtots[0].pop()
carry2=bigtots[1].pop()
acgen=[bigtots[0],bigtots[1],[],[] ]
while carry1 != maxscore: ## use +1 on the end of max score for debug
    oldone=acgen[0]
    oldtwo=acgen[1]
    freshone= acgen[0][:int(len(acgen[0])/2)]+acgen[1][int(len(acgen[1])/2):]
    freshtwo= acgen[1][:int(len(acgen[1])/2)]+acgen[0][int(len(acgen[0])/2):]
    t=random.randint(0,wordlen)
    mutone=acgen[0]
    muttwo=acgen[1]
    mutone[t]=chr(random.randint(0,dataset))
    muttwo[t]=chr(random.randint(0,dataset))
    acgen=[oldone,oldtwo,freshone,freshtwo,mutone,muttwo]
    for o in range (1,5):
        comparison = []
        loopone=random.randint(wordlen,wordlen) #If testing is required, then change to 4
        for p in range(loopone):
            #ascii charater codes to letters
            x=random.randint(0,dataset)
            z=chr(x)
            comparison.append(z)
        comparison.append(loopone)
        acgen.append(comparison)
    #weighting comparisons
    tots=[]
    carry=[]
    for k in acgen:
        score=0
        runner=0
        #length scores
        if k[-1] == wordlen:
            score+=1
        #character confirmation
        try:
            for l in word:
                if k[runner] == word[runner]:
                    score+=1
                    runner+=1
                else:
                    runner+=1
        except:
            IndexError
        k.append(score)
        tots.append(k)
    acgen=sorted(tots,key=lambda change:change[-1], reverse=True)
    
    for q in acgen:
        AAAAAA=q.pop()
        carry.append(AAAAAA)
    carry1=carry[0]
    print(carry1)
    print(acgen)
    #print(carry1)
    #while final index isnt equal to max score, iterate


    #function that has: letters and length (number of iterations) as variables
stop=time()
print("time taken is ",(stop-start),"seconds")