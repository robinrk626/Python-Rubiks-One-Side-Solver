import copy
ans=[]
ansMoves=5
def calc(arr,res,nMove):
    global ansMoves
    global ans
    if arr[0]==arr[1]==arr[2] and arr[3]==arr[4]==arr[5] and arr[6]==arr[7]==arr[8] and nMove<ansMoves:
        ans= copy.deepcopy(res)
        ans.append(arr)
        ansMoves= nMove
        return 
    if arr in res:
        return

    if nMove<ansMoves:
        calc([arr[1],arr[2],arr[0],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8]],res+[arr],nMove+1)
        calc([arr[0],arr[1],arr[2],arr[4],arr[5],arr[3],arr[6],arr[7],arr[8]],res+[arr],nMove+1)
        calc([arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[7],arr[8],arr[6]],res+[arr],nMove+1)
        calc([arr[2],arr[0],arr[1],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8]],res+[arr],nMove+1)
        calc([arr[0],arr[1],arr[2],arr[5],arr[3],arr[4],arr[6],arr[7],arr[8]],res+[arr],nMove+1)
        calc([arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[8],arr[6],arr[7]],res+[arr],nMove+1)
        calc([arr[3],arr[1],arr[2],arr[6],arr[4],arr[5],arr[0],arr[7],arr[8]],res+[arr],nMove+1)
        calc([arr[0],arr[4],arr[2],arr[3],arr[7],arr[5],arr[6],arr[1],arr[8]],res+[arr],nMove+1)
        calc([arr[0],arr[1],arr[5],arr[3],arr[4],arr[8],arr[6],arr[7],arr[2]],res+[arr],nMove+1)
        calc([arr[6],arr[1],arr[2],arr[0],arr[4],arr[5],arr[3],arr[7],arr[8]],res+[arr],nMove+1)
        calc([arr[0],arr[7],arr[2],arr[3],arr[1],arr[5],arr[6],arr[4],arr[8]],res+[arr],nMove+1)
        calc([arr[0],arr[1],arr[8],arr[3],arr[4],arr[2],arr[6],arr[7],arr[5]],res+[arr],nMove+1)

cube=['G','G','B','G','B','B','R','R','R']
calc(cube,[],0)
i=0
for _ in ans: 
    print('After ',i,' move:  ')
    print(_[0],'  ',_[1],'  ',_[2])
    print(_[3],'  ',_[4],'  ',_[5])
    print(_[6],'  ',_[7],'  ',_[8])
    i=i+1
#Dipesh Bindlish
#Robin Garg
