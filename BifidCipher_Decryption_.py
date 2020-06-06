plain_txt = input("Enter The Plain Text :  ")
key = input("Enter The KEY : ")
key = key.upper()
plain_txt = plain_txt.upper()

# meet me at toga party

alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
pln_txt= ""

for i in plain_txt:
    if i in alphas:
        pln_txt+=(i)

''' creating a liest of key'''
key_alp_all_comon = list()
for i in key:
    for j in alphas:
        if i == j:
            key_alp_all_comon.append(i)

''' creating a liest of key with only one value'''
key_alp_comon = list()
for k in key_alp_all_comon:
    if k not in key_alp_comon:
        key_alp_comon.append(k)

''' creating a liest of alpha witout key'''
alphas_alon = list()
for i in alphas:
    if i not in key_alp_comon:
        alphas_alon.append(i)

''' creating a matrix list'''
mat = key_alp_comon + alphas_alon
for k in mat:
    if k == 'J':
        mat.remove(k)

''' creating a matrix'''
matrix = [[0 for i in range(5)] for j in range(5)]
ind = 0
for i in range(5):
    for j in range(5):
        matrix[i][j] = mat[ind]
        ind+=1

RC = list()
for ii in range(int(len(pln_txt))):
        for i in range(5):
            for j in range(5):
                if pln_txt[ii] == matrix[i][j]:
                    RC.append(i)
                    RC.append(j)
lrc=0
lr=0
lc=0
R1 = list()
C1 = list()
while lrc < int(len(RC)):
    for i in range(int(len(key))):
        if lr < int(len(pln_txt)):
            R1.append(int(RC[lrc]))
            lrc+=1
            lr+=1

    for i in range(int(len(key))):
        if lc < int(len(pln_txt)):
            C1.append(int(RC[lrc]))
            lrc+=1
            lc+=1

cip_txt=""
for i in range(0,int(len(R1))):
    ii = R1[i]
    jj = C1[i]
    cip_txt+=matrix[ii][jj]


'''AEAMSUPSQWDUABWXY'''
print(cip_txt)