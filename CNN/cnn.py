data = [[3, 3, 2, 1, 0], [0, 0, 1, 3, 1], [3, 1, 2, 2, 3], [2, 0 ,0, 2, 2], [2, 0, 0, 0, 1]]
kermat = [[0, 1, 2], [2, 2, 0], [0, 1, 2]]

def dotprod(A,B):
    #print(A)
    #print('\n\n')
    #print(B)
    sum = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            sum += A[i][j]*B[i][j]
    return sum

def kernel(mat,ker,stride):
    kersize = len(ker)
    op=[]
    x=0
    for i in range((len(mat)-kersize)+1):
        if x%stride == 0:
            optp=[]
            y=0
            for j in range((len(mat)-kersize)+1):
                if y%stride == 0:
                    A=[]
                    for ro in range(kersize):
                        temp=[]
                        for co in range(kersize):
                            temp.append(mat[i+ro][j+co])
                        A.append(temp)
                    optp.append(dotprod(A,ker))
                y+=1
            op.append(optp)
        x+=1
    return op

def padding(mat):
    temp = [0 for _ in range(len(mat)+2)]
    op= []
    op.append(temp)
    for i in range(len(mat)):
        optp = [0]
        for j in range(len(mat[i])):
            optp.append(mat[i][j])
        optp.append(0)
        op.append(optp)
    op.append(temp)
    return op

def pooling(mat,pooler,poolwala=0):
    op = []
    x=0
    for i in range((len(mat)//pooler)+1):
        if x%pooler == 0:
            optp = []
            y=0
            for j in range((len(mat)//pooler)+1):
                newmat = []
                if y%pooler == 0:
                    for ro in range(pooler):
                        for co in range(pooler):
                            newmat.append(mat[i+ro][j+co])
                    #print(newmat)
                    if poolwala == 0:
                        optp.append(max(newmat))
                    else:
                        optp.append(sum(newmat)/len(newmat))
                y+=1
            op.append(optp)
        x+=1
    return op

#print(padding(data))
#print(kernel(padding(data),kermat,1))
print(pooling(kernel(padding(data),kermat,1),2,0))
