n=int(input('Choose your number: '))


def createTable (number) :
    b=[]
    for i in range(number):
        b.append([])
        for j in range(number):
            b[i].append(0)
    return b

def printTable (number, bo) :
    for i in range(number):
        for j in range(number):
            if bo[i][j]=="Q":
                print (bo[i][j], end=" ")
            else:
                print (0, end=" ")
        print("")

def Queen(number, bo, pos, sign):
    for i in range(0, number):
        if sign==-1 and bo[i][pos[1]]!=0:    
            bo[i][pos[1]]+=sign
        if sign==1 :
            bo[i][pos[1]]+=sign   
    for i in range(0, number):
        if sign==-1 and bo[pos[0]][i]!=0:    
            bo[pos[0]][i]+=sign
        if sign==1 :
            bo[pos[0]][i]+=sign 
    j=pos[1]
    k=pos[0]
    l=pos[1]
    m=pos[0]
    
    js=pos[1]
    ks=pos[0]
    ls=pos[1]
    ms=pos[0]
    
    for i in range(0, number):
            if j<number and m<number :
                if sign==-1 and bo[m][j]!=0:    
                    bo[m][j]+=sign
                if sign==1 :
                    bo[m][j]+=sign
                j+=1
                m+=1
            if k>=0 and l>=0 :
                if sign==-1 and bo[k][l]!=0:    
                    bo[k][l]+=sign
                if sign==1 :
                    bo[k][l]+=sign
                k-=1
                l-=1
            if ks>=0 and ls<number :
                if sign==-1 and bo[ks][ls]!=0:    
                    bo[ks][ls]+=sign
                if sign==1 :
                    bo[ks][ls]+=sign
                ks-=1
                ls+=1
            if ms<number and js>=0 :
                if sign==-1 and bo[ms][js]!=0:    
                    bo[ms][js]+=sign
                if sign==1 :
                    bo[ms][js]+=sign
                ms+=1
                js-=1

def checkNoQueens(number, bo):
    k=0
    for i in range(number):
        for j in range(number):
            if bo[i][j] == "Q" :
                k+=1
    return k

  

def solve(number, bo):
    n=checkNoQueens(number,bo)
    if n==number:
        return True
    else:
        for index in range(number):
            for jindex in range(number):
                if bo[index][jindex] == 0:
                    Queen(number,bo,(index, jindex), 1)
                    bo[index][jindex]="Q"
                    if solve(number, bo):
                        return True
                    bo[index][jindex]=6
                    Queen(number,bo,(index, jindex), -1)
    return False

board = createTable(n)
solve(n, board)
printTable(n, board)
y= checkNoQueens(n,board)
print(y)